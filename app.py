from flask import Flask, render_template as rt, request, redirect, url_for
from models import *
from apis import *
import os
from flask_restful import Api

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "database.sqlite3")

db.init_app(app)
app.app_context().push()

api = Api(app)
api.add_resource(campaign, '/api/campaign')    
api.add_resource(ad_request, '/api/ad_request')

current_userID = None

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":

        user_data = User.query.filter(User.email == request.form['email']).first()
        if user_data:
            if user_data.password == request.form['password']:
                global current_userID

                if user_data.is_flagged:
                    return rt('index.html', message = "You have been flagged for misconduct!! Contact Admin for further details")

                if user_data.role == 'influencer':
                    current_userID = user_data.id
                    return redirect(url_for('idashboard'))
                
                elif user_data.role == 'sponsor':
                    current_userID = user_data.id
                    return redirect(url_for('sdashboard'))
                
                elif user_data.role == 'admin':
                    current_userID = user_data.id
                    return redirect(url_for('admin_dashboard'))
                
            else:
                return rt('index.html', message = "Invalid Password!")
        else:
            return rt('index.html', message = "Invalid Email!")
        
    return rt('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']

        if User.query.filter(User.email == email).first():
            return rt('signup.html', message="Email already registered!")

        new_user = User(username = request.form['username'], email = email, role = role, password = request.form['password'])
        db.session.add(new_user)
        db.session.commit() 

        if role == 'influencer':
            new_profile = Profile(user_id = new_user.id, 
                                  name = request.form['name'], 
                                  industry = request.form['industry'], 
                                  niche = request.form['niche'], 
                                  reach = request.form['reach'], 
                                  funds= 0.0)
        
        elif role == 'sponsor':
            new_profile = Profile(user_id = new_user.id, 
                                  name = request.form['name'], 
                                  industry = request.form['industry'], 
                                  niche = request.form['niche'], 
                                  funds = request.form['funds'])

        db.session.add(new_profile)
        db.session.commit()    

        return rt('index.html', message = "User Account Created Successfully")
    return rt('signup.html')


@app.route('/idashboard', methods = ['GET', 'POST'])
def idashboard():

    inf = Profile.query.filter(Profile.user_id == current_userID).first()
    name = inf.name
    funds = inf.funds
    ad_requests = AdRequest.query.filter(
        AdRequest.influencer_id == current_userID, 
        AdRequest.initiator == 'sponsor', 
        AdRequest.status == 'Pending').all()
    requests_data = []
    for request in ad_requests:
        requests_data.append({
            'campaign_title': request.campaign.title,
            'sponsor_name': request.name,
            'request_id': request.id
        })

    today = datetime.today()
    ads= AdRequest.query.filter(
        AdRequest.influencer_id == current_userID, 
        AdRequest.status == 'accepted').all()
    campaign_ids = [ad.campaign_id for ad in ads]
    dat = Campaign.query.filter(Campaign.id.in_(campaign_ids)).all()
    for campaign in dat:
        campaign.end_date = campaign.get_end_date()
        campaign.progress = campaign.get_progress()

    active_campaigns = [campaign for campaign in dat if datetime.strptime(campaign.start_date, "%Y-%m-%d") 
                        <= today <= datetime.strptime(campaign.end_date, "%Y-%m-%d")]

    today_date = today.strftime("%Y-%m-%d")
    return rt('idashboard.html', 
              name =name, 
              funds = funds, 
              campaigns = active_campaigns, 
              requests = requests_data, 
              today_date = today_date, 
              userID = current_userID)

@app.route('/find_influencer', methods = ['GET', 'POST'])
def find_influencer():
    if request.method == 'POST':
        search_tag = request.form['tag']
        search_input = request.form['search-input'] 
        source = request.form['source']
        print(current_userID)

        if search_tag == 'title':
            data = Campaign.query.filter(Campaign.title.like('%' + search_input + '%'), Campaign.visibility == 'public').all()
        elif search_tag == 'description':
            data = Campaign.query.filter(Campaign.description.like('%' + search_input + '%'), Campaign.visibility == 'public').all()
        elif search_tag == 'funds':
            data = Campaign.query.filter(Campaign.funds >= search_input, Campaign.visibility == 'public').all()

        for campaign in data:
            campaign.end_date = campaign.get_end_date()
            campaign.progress = campaign.get_progress()

        today_date = datetime.today().strftime("%Y-%m-%d")
        if source == 'influencer':
            return rt('find_influencer.html', campaigns=data, userID=current_userID, today_date=today_date)
        
    
    return rt('find_influencer.html')


@app.route('/sdashboard', methods = ['GET', 'POST'])
def sdashboard():

    sponsor = Profile.query.filter(Profile.user_id == current_userID).first()
    name = sponsor.name

    today = datetime.today()
    dat = Campaign.query.filter(Campaign.sponsor_id == current_userID).all()
    for campaign in dat:
        campaign.end_date = campaign.get_end_date()
        campaign.progress = campaign.get_progress()

    active_campaigns = [campaign for campaign in dat if datetime.strptime(campaign.start_date, "%Y-%m-%d") 
                        <= today <= datetime.strptime(campaign.end_date, "%Y-%m-%d")]
    

    ad_requests = AdRequest.query.join(Campaign).filter(
        Campaign.sponsor_id == current_userID,
        AdRequest.initiator == 'influencer',
        AdRequest.status == 'Pending').all()    
    
    requests_data = []
    for request in ad_requests:
        influencer = User.query.filter(User.id == request.influencer_id).first()
        requests_data.append({
            'campaign_title': request.campaign.title,
            'influencer_username': influencer.username,
            'request_id': request.id
        })
    
    today_date = today.strftime("%Y-%m-%d")
    return rt('sdashboard.html', 
              name =name, 
              campaigns = active_campaigns, 
              requests = requests_data, 
              today_date = today_date, 
              userID = current_userID)


@app.route('/scampaigns', methods = ['GET', 'POST'])
def scampaigns():

    dat = Campaign.query.filter(Campaign.sponsor_id == current_userID).all()
    for campaign in dat:
        campaign.end_date = campaign.get_end_date()
        campaign.progress = campaign.get_progress()

    today_date = datetime.today().strftime("%Y-%m-%d")

    return rt('campaign_sponsor.html', campaigns = dat, today_date = today_date, userID = current_userID)


@app.route('/view_details/<source>/<int:id>', methods=['POST'])
def view_details(id, source):
    if source =='campaign':
        campaign = Campaign.query.filter(Campaign.id == id).first()
        campaign.end_date = campaign.get_end_date()
        campaign.progress = campaign.get_progress()
        today_date = datetime.today().strftime("%Y-%m-%d")
        print(today_date)
        print(current_userID)
        if campaign:
            return rt('view_details.html', campaign=campaign, today_date = today_date, userID = current_userID)
        else:
            return 'Campaign not found', 404


@app.route('/view_requests/<source>/<int:id>', methods=['POST'])
def view_requests(id, source):
    if source == 'campaign':
        
        requests = AdRequest.query.filter(AdRequest.campaign_id == id).all()
        for request in requests:
            inf = User.query.filter(User.id == request.influencer_id).first()
            request.inf_username = inf.username
            if request.status == 'accepted':
                request.status = 'Accepted by Influencer' if request.initiator == 'sponsor' else 'Accepted by You'
        return rt('view_requests.html', requests=requests, campaign_id=id, userID = current_userID)

    elif source == 'requests':
        campaigns = Campaign.query.filter(Campaign.sponsor_id == id).all()
        requests =[]
        for campaign in campaigns:
            request = AdRequest.query.filter(AdRequest.campaign_id == campaign.id).all()
            for req in request:
                inf = User.query.filter(User.id == req.influencer_id).first()
                req.inf_username = inf.username
                if req.status == 'accepted':
                    req.status = 'Accepted by Influencer' if req.initiator == 'sponsor' else 'Accepted by You'
                requests.append(req)
        print(requests)
        return rt('view_requests.html', requests=requests, campaign_id=id, userID = current_userID)

@app.route('/find_sponsor', methods = ['GET', 'POST'])
def find_sponsor():
    if request.method == 'POST':
        search_tag = request.form['tag']
        search_input = request.form['search-input'] 
        print(current_userID)

        if search_tag == 'title':
            data = Campaign.query.filter(Campaign.title.like('%' + search_input + '%'), Campaign.visibility == 'public').all()
            for campaign in data:
                campaign.end_date = campaign.get_end_date()
                campaign.progress = campaign.get_progress()

        elif search_tag == 'username':
            users = User.query.filter(User.username.like('%' + search_input + '%'), User.role == 'influencer').all()
            data = []
            for user in users:
                profile = Profile.query.filter(Profile.user_id==user.id).first()
                data.append(profile)


        today_date = datetime.today().strftime("%Y-%m-%d")
        return rt('find_sponsor.html', results=data, userID = current_userID, today_date=today_date, tag = search_tag)

    return rt('find_sponsor.html')



@app.route('/update_request_status/<source>/<int:request_id>', methods=['POST'])
def update_request_status(request_id, source):
    action = request.form['action']
    ad_request = AdRequest.query.filter(AdRequest.id == request_id).first()

    if not ad_request:
        return {'message': 'Ad request not found'}, 404

    if action == 'accept':
        if source == 'sponsor':
            accptReq = AdRequest.query.filter(
                AdRequest.campaign_id == ad_request.campaign_id,
                AdRequest.status == 'accepted'
            ).all()
            totalPayments = sum(request.payment_amount for request in accptReq)
            print(totalPayments)
            campaign = Campaign.query.filter(Campaign.id == ad_request.campaign_id).first()
            if not campaign:
                return {'message': 'Campaign not found'}, 404

            remFunds = campaign.funds - totalPayments
            print(remFunds)
            
            if remFunds >= ad_request.payment_amount:
                ad_request.status = 'accepted'
                infProfile = Profile.query.filter(Profile.user_id == ad_request.influencer_id).first()
                if not infProfile:
                    return {'message': 'Influencer profile not found'}, 404

                infProfile.funds += ad_request.payment_amount
            else:
                return {'message': 'Insufficient campaign funds to accept this request'}, 400

        elif source == 'influencer':
            ad_request.status = 'accepted'
            infProfile = Profile.query.filter(Profile.user_id == ad_request.influencer_id).first()
            if not infProfile:
                return {'message': 'Influencer profile not found'}, 404

            infProfile.funds += ad_request.payment_amount

    elif action == 'reject':
        ad_request.status = 'rejected'

    db.session.commit()
    if source == 'sponsor':
        return redirect(url_for('sdashboard'))
    elif source == 'influencer': 
        return redirect(url_for('idashboard'))





@app.route('/admin_dashboard', methods = ['GET', 'POST'])
def admin_dashboard():

    all_campaigns = Campaign.query.all()
    today = datetime.today()
    ongoing_campaigns = [
        campaign for campaign in all_campaigns
        if datetime.strptime(campaign.start_date, "%Y-%m-%d") <= today <= datetime.strptime(campaign.get_end_date(), "%Y-%m-%d")
    ]
    for campaign in ongoing_campaigns:
        campaign.end_date = campaign.get_end_date()
        campaign.progress = campaign.get_progress()
    
    public_campaigns = [campaign for campaign in all_campaigns if campaign.visibility == 'public']
    private_campaigns = [campaign for campaign in all_campaigns if campaign.visibility == 'private']
    flagged_users = User.query.filter(User.is_flagged == True).all()
    total_users = User.query.filter(User.role != 'admin').count()
    influencers = User.query.filter(User.role == 'influencer').count()  
    sponsors = User.query.filter(User.role == 'sponsor').count()
    
    return rt('admin_dashboard.html', 
              total_campaigns=len(all_campaigns),
              active_campaigns=len(ongoing_campaigns),
              public_campaigns=len(public_campaigns),
              private_campaigns=len(private_campaigns),
              total_users=total_users,
              influencers=influencers,
              sponsors=sponsors,
              flagged_users=len(flagged_users))


@app.route('/show_campaigns/<type>')
def show_campaigns(type):
    if type == 'all':
        campaigns = Campaign.query.all()
    elif type == 'active':
        today = datetime.today()
        temp = Campaign.query.all()
        for campaign in temp:
            campaign.end_date = campaign.get_end_date()
            campaign.progress = campaign.get_progress()
        campaigns = [campaign for campaign in temp if datetime.strptime(campaign.start_date, "%Y-%m-%d") 
                     <= today <= datetime.strptime(campaign.end_date, "%Y-%m-%d")]
    elif type == 'public':
        campaigns = Campaign.query.filter(Campaign.visibility == 'public').all()
    elif type == 'private':
        campaigns = Campaign.query.filter(Campaign.visibility == 'private').all()

    for campaign in campaigns:
        campaign.end_date = campaign.get_end_date()
        campaign.progress = campaign.get_progress()
    today_date = datetime.today().strftime("%Y-%m-%d")
    return rt('campaigns.html', campaigns=campaigns, today_date = today_date)


@app.route('/show_users/<type>', methods=['GET', 'POST'])
def show_users(type):
    if type == 'all':
        users = User.query.filter(User.role != 'admin').all()
    elif type == 'influencers':
        users = User.query.filter(User.role == 'influencer').all()
    elif type == 'sponsors':
        users = User.query.filter(User.role == 'sponsor').all()
    elif type == 'flagged':
        users = User.query.filter(User.is_flagged == True).all()
    
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        action = request.form.get('action')
        user = db.session.get(User, user_id)
        print(user_id)
        print(action)
        print(user)
        print("Before", user.is_flagged)
        if user:
            if action == 'flag':
                user.flag()
            elif action == 'unflag':
                user.unflag()
            print(user.is_flagged)
            db.session.commit()
        print("AFTER", user.is_flagged) 
        return redirect(url_for('show_users', type=type))
    
    return rt('users.html', users=users, type=type)


@app.route('/search_admin', methods = ['GET', 'POST'])
def search_admin():
    if request.method == 'POST':
        source = request.form['source']
        search_tag = request.form['tag']
        search_input = request.form['search-input'] 
        print(current_userID)

        if source == 'campaigns':
            if search_tag == 'title':
                data = Campaign.query.filter(Campaign.title.like('%' + search_input + '%')).all()
                for campaign in data:
                    campaign.end_date = campaign.get_end_date()
                    campaign.progress = campaign.get_progress()

            elif search_tag == 'progress':
                all_campaigns = Campaign.query.all()
                for campaign in all_campaigns:
                    campaign.end_date = campaign.get_end_date()
                    campaign.progress = campaign.get_progress()
                
                data = [campaign for campaign in all_campaigns if campaign.progress >= float(search_input)]
            
            elif search_tag == 'funds':
                data = Campaign.query.filter(Campaign.funds >= search_input).all()
                for campaign in data:
                    campaign.end_date = campaign.get_end_date()
                    campaign.progress = campaign.get_progress()
                
        elif source == 'users':
            if search_tag == 'username':
                users = User.query.filter(User.username.like('%' + search_input + '%'), User.role != 'admin').all()
                data = []
                for user in users:
                    profile = Profile.query.filter(Profile.user_id==user.id).first()
                    data.append(profile)
            elif search_tag == 'role':
                users = User.query.filter(User.role == search_input).all()
                data = []
                for user in users:
                    profile = Profile.query.filter(Profile.user_id==user.id).first()
                    data.append(profile)
            
            elif search_tag == 'funds':
                users = db.session.query(User).join(Profile).filter(Profile.funds >= search_input).all()
                data = []
                for user in users:
                    profile = Profile.query.filter(Profile.user_id == user.id).first()
                    data.append(profile)

        today_date = datetime.today().strftime("%Y-%m-%d")
        return rt('search_admin.html', results=data, userID = current_userID, today_date=today_date, source = source)

    return redirect(url_for('admin_dashboard'))


@app.route('/logout')
def logout():
    global current_userID
    current_userID = None
    return redirect(url_for('index'))


if __name__ =='__main__':
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0')