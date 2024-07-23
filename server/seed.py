from config import app, db
from models.user import User
from models.trip import Trip
from models.entry import Entry

with app.app_context():
    User.query.delete()
    Trip.query.delete()
    Entry.query.delete()

    user1 = User(name='Taylor', username='tayloruser')
    user1.password_hash = 'abc123'
    user2 = User(name='Spencer', username='spenceruser')
    user2.password_hash = 'xyz789'
    user3 = User(name='Nancy', username='nancyuser')
    user3.password_hash = 'mno456'
    user4 = User(name='Arthur', username='arthuruser')
    user4.password_hash = 'pqr246'
    db.session.add_all([user1, user2, user3, user4])
    db.session.commit()

    trip1 = Trip(name='Appalachian Trail', country='United States', total_miles=2168)
    trip2 = Trip(name='Great Wall of China', country='China', total_miles=13171)
    trip3 = Trip(name='Nile River', country='Egypt', total_miles=4130)
    trip4 = Trip(name='Macchu Pichu', country='Peru', total_miles=26)
    db.session.add_all([trip1, trip2, trip3, trip4])
    db.session.commit()

    entry1 = Entry(date='07-02-24', miles=4.5, user_id=1, trip_id=2)
    entry2 = Entry(date='07-05-24', miles=2.6, user_id=2, trip_id=3)
    entry3 = Entry(date='07-12-24', miles=7.3, user_id=3, trip_id=2)
    entry4 = Entry(date='07-22-24', miles=5.2, user_id=4, trip_id=4)
    db.session.add_all([entry1, entry2, entry3, entry4])
    db.session.commit()