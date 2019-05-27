from core.models.models import db, Game, Type, Destination, Channel, Clip, Video, VideoClips

if __name__ == "__main__":
    db.connect()
    db.create_tables([Game, Type, Destination, Channel, Clip, Video, VideoClips])

    Type.create(name='day')
    Type.create(name='week')
    Type.create(name='month')
    Type.create(name='compilation')
    Type.create(name='all')

    Game.create(name='Fortnite', full='Fortnite', cli='fortnite')
    Game.create(name='Twitch' , full='Twitch', cli='twitch')    
    Game.create(name='Just%20Chatting', full='Just Chatting', cli='just chatting')
    Game.create(name='Super%20Smash%20Bros.%20Ultimate', full='Super Smash Bros. Ultimate', cli='supersmashbrothers')
    Game.create(name='Escape%20From%20Tarkov', full='Escape From Tarkov', cli='eft')
