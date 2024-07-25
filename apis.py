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


        if Campaign.query.filter(Campaign.title == args['title']).first():
            return {'message' : 'Campaigns cannot have duplicate titles'}, 404
        

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

        # Retrieve the existing campaign from the database
        existing_campaign = Campaign.query.filter(Campaign.id == args['campaign_id']).first()

        if not existing_campaign:
            return {'message': 'Campaign not found'}, 404

        # Update the existing campaign object
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

        print(del_campaign)
        db.session.delete(del_campaign)
        db.session.commit()

        return {'message': 'Campaign deleted successfully!'}
 

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

        new_req = AdRequest(name = args['name'], campaign_id=args['campaign_id'], initiator = args['initiator'], messages=args['messages'], payment_amount=args['payment_amount'], status='Pending')
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