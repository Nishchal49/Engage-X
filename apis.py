from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError
from models import *

class campaign(Resource):
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('description', type=str, required=True, help='Description is required')
        parser.add_argument('goals', type=str, required=True, help='Goals are required')
        parser.add_argument('funds', type=float, required=True, help='Funds is required')
        parser.add_argument('start_date', type=str, required=True, help='Start date is required')
        parser.add_argument('days', type=int, required=True, help='Duration in days is required')
        parser.add_argument('visibility', type=str, required=True, help='Visibility is required')
        parser.add_argument('sponsor_id', type=int, required=False, help='User ID is required')
        args = parser.parse_args()

        spons = Profile.query.filter(Profile.user_id == args['sponsor_id']).first()
        if not spons:
            return {'message': 'Sponsor does not exist'}, 400
        
        total_funds = spons.funds
        print(total_funds)

        if total_funds < args['funds']:
            return {'message': 'Insufficient funds'}, 400
        
        spons.funds -= args['funds']

        
        if Campaign.query.filter(Campaign.title == args['title']).first():
            return {'message' : 'Campaigns cannot have duplicate titles'}, 404

        new_campaign = Campaign(
            title=args['title'],
            description=args['description'],
            goals=args['goals'],
            funds=args['funds'],
            start_date=args['start_date'],
            days=args['days'],
            visibility=args['visibility'],
            sponsor_id=args['sponsor_id']
        )

        print(new_campaign.title)
        print(new_campaign.description)
        print(new_campaign.goals)
        print(new_campaign.funds)
        print(new_campaign.start_date)
        print(new_campaign.days)
        print(new_campaign.visibility)
        print(new_campaign.sponsor_id)


        db.session.add(new_campaign)
        db.session.commit()

        return {'message' : 'Campaign created successfully!'}
    
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('description', type=str, required=True, help='Description is required')
        parser.add_argument('goals', type=str, required=True, help='Goals are required')
        parser.add_argument('funds', type=float, required=True, help='Funds is required')
        parser.add_argument('start_date', type=str, required=True, help='Start date is required')
        parser.add_argument('days', type=int, required=True, help='Duration in days is required')
        parser.add_argument('visibility', type=str, required=True, help='Visibility is required')
        parser.add_argument('sponsor_id', type=int, required=False, help='User ID is required')
        parser.add_argument('campaign_id', type=int, required=False, help='Campaign ID is required')
        args = parser.parse_args()

        existing_campaign = Campaign.query.filter(Campaign.id == args['campaign_id']).first()

        if not existing_campaign:
            return {'message': 'Campaign not found'}, 404
        
        spons = Profile.query.filter(Profile.user_id == args['sponsor_id']).first()
        if not spons:
            return {'message': 'Sponsor does not exist'}, 400
        
        total_funds = spons.funds + existing_campaign.funds
        print(total_funds)

        if total_funds < args['funds']:
            return {'message': 'Insufficient funds'}, 400
        
        spons.funds = total_funds - args['funds']

        existing_campaign.title = args['title']
        existing_campaign.description = args['description']
        existing_campaign.goals = args['goals']
        existing_campaign.funds = args['funds']
        existing_campaign.start_date = args['start_date']
        existing_campaign.days = args['days']
        existing_campaign.visibility = args['visibility']
        existing_campaign.sponsor_id = args['sponsor_id']

        try:
            db.session.commit()
            return {'message': 'Campaign updated successfully!'}
        except IntegrityError as e:
            db.session.rollback()
            return {'message': 'Error updating campaign: {}'.format(str(e))}, 500
        
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='Campaign ID is required')
        args = parser.parse_args()

        del_campaign = Campaign.query.get(args['id'])
        if not del_campaign:
            return {'message': 'Campaign not found'}, 404
        
        today = datetime.today().strftime("%Y-%m-%d")
        end_date = del_campaign.get_end_date()

        if today <= end_date:
            spons = Profile.query.filter(Profile.user_id == del_campaign.sponsor_id).first()
            if not spons:
                return {'message': 'Sponsor does not exist'}, 400
            spons.funds += del_campaign.funds

        print(del_campaign)
        db.session.delete(del_campaign)
        db.session.commit()

        return {'message': 'Campaign deleted successfully!'}
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='Campaign ID is required')
        args = parser.parse_args()

        campaign = Campaign.queryfilter(Campaign.id == args['id'])
        if not campaign:
            return {'message': 'Campaign not found'}, 404
        
        return {
            'id': campaign.id,
            'title': campaign.title,
            'description': campaign.description,
            'goals': campaign.goals,
            'funds': campaign.funds,
            'start_date': campaign.start_date,
            'days': campaign.days,
            'visibility': campaign.visibility,
            'sponsor_id': campaign.sponsor_id,
            'message': 'Campaign details retrieved successfully!'
        }

 

class ad_request(Resource):
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name is required')
        parser.add_argument('campaign_id', type=int, required=True, help='Campaign ID is required')
        parser.add_argument('initiator', type=str, required=True, help='Initiator is required')
        parser.add_argument('messages', type=str, required=True, help='Messages are required')
        parser.add_argument('requirements', type=str, required=False) # Optional field for sponsor dashboard
        parser.add_argument('payment_amount', type=float, required=True, help='Payment amount is required')
        parser.add_argument('userId', type=int, required=False, help='User ID is required')
        parser.add_argument('inf_name', type=str, required=False)
        args = parser.parse_args()

        if args['initiator'] == 'sponsor':
            accptReq = AdRequest.query.filter(
                AdRequest.campaign_id == args['campaign_id'],
                AdRequest.status == 'accepted'
            ).all()
            totalPayments = sum(request.payment_amount for request in accptReq)
            print(totalPayments)
            campaign = Campaign.query.filter(Campaign.id == args['campaign_id']).first()
            if not campaign:
                return {'message': 'Campaign not found'}, 404

            remFunds = campaign.funds - totalPayments
            print(remFunds)

            if remFunds < args['payment_amount']:
                return {'message': 'Insufficient campaign funds to offer this payment amount'}, 400



        new_req = AdRequest(name = args['name'], 
                            campaign_id=args['campaign_id'], 
                            initiator = args['initiator'], 
                            messages=args['messages'], 
                            payment_amount=args['payment_amount'], 
                            status='Pending')
        
        if args['userId']:
            new_req.influencer_id=args['userId']

        else:
            inf = User.query.filter(User.username == args['inf_name']).first()
            if inf:
                new_req.requirements = args['requirements']
                new_req.influencer_id= inf.id
                print(new_req.requirements)
                print(new_req.influencer_id)
            else:
                return {'message' : 'User not found!'}, 404

        print(new_req.name)
        print(new_req.campaign_id)  
        print(new_req.influencer_id)
        print(new_req.initiator)
        print(new_req.messages)
        print(new_req.payment_amount)
        print(new_req.status)
        

        db.session.add(new_req)
        db.session.commit()


        return {'message' : 'Request sent!'}