from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False) # admin , sponsor or influencer
    password = db.Column(db.String, nullable=False)
    is_flagged = db.Column(db.Boolean, default=False, nullable=False)  # New attribute for flagging users

    profile = db.relationship('Profile', back_populates='user', uselist=False)
    campaigns = db.relationship('Campaign', back_populates='sponsor')
    ad_requests = db.relationship('AdRequest', back_populates='influencer')
    
    def flag(self):
        if self.role == 'admin':
            raise PermissionError("Admins cannot flag their own account.")
        self.is_flagged = True
        db.session.commit()

    def unflag(self):
        self.is_flagged = False
        db.session.commit()




class Profile(db.Model):
    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    industry = db.Column(db.String)
    niche = db.Column(db.String)

    reach = db.Column(db.Integer)
    funds = db.Column(db.Float)

    user = db.relationship('User', back_populates='profile')




class AdRequest(db.Model):
    __tablename__ = "ad_request"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    influencer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey("campaign.id"), nullable=False)
    initiator = db.Column(db.String, nullable=False) # sponosr, influencer
    name = db.Column(db.String, nullable = False)
    messages = db.Column(db.Text)
    requirements = db.Column(db.Text)
    payment_amount = db.Column(db.Float, nullable=False)

    status = db.Column(db.String, nullable=False, default='Pending')  # pending, accepted or rejected

    campaign = db.relationship('Campaign', back_populates='ad_requests')
    influencer = db.relationship('User', back_populates='ad_requests')




class Campaign(db.Model):
    __tablename__ = "campaign"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sponsor_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    goals = db.Column(db.Text, nullable=False)

    start_date = db.Column(db.String, nullable=False)
    days = db.Column(db.Integer, nullable=False)
    funds = db.Column(db.Float, nullable=False)

    visibility = db.Column(db.String, nullable=False)  # public or private

    sponsor = db.relationship('User', back_populates='campaigns')
    ad_requests = db.relationship('AdRequest', back_populates='campaign')
    
    def get_end_date(self):
        start_date_obj = datetime.strptime(self.start_date, "%Y-%m-%d")
        end_date_obj = start_date_obj + timedelta(days=self.days)
        return end_date_obj.strftime("%Y-%m-%d")

    def get_progress(self):
        start_date_obj = datetime.strptime(self.start_date, "%Y-%m-%d")
        today = datetime.today()
        elapsed_days = (today - start_date_obj).days
        progress = "{:.2f}".format((elapsed_days / self.days) * 100)  # Format progress to 2 decimal places
        progress = min(max(float(progress), 0), 100)  # Ensure progress is between 0 and 100
        return progress