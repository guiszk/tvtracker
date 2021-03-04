from pushbullet.pushbullet import PushBullet

apiKey = "[API KEY]"
p = PushBullet(apiKey)

devices = p.getDevices()
contacts = p.getContacts()

def sendalert(title, body):
    p.pushNote(devices[0]["iden"], title, body)
