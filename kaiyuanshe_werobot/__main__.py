import werobot

robot = werobot.WeRoBot(token='weixin')


@robot.text
def hello_world():
    return 'Hello World!'


def main():
    robot.run(port=8000)
