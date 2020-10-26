import os
import speedtest

def notification(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


test = speedtest.Speedtest()
print('You will see your download speed, upload speed and ping to a close by server')

download_speed = test.download()
upload_speed = test.upload()

server = []
test.get_servers(server)
server_results = test.results.ping

# using function to make notification
notification(title  = 'Network Tester',
       subtitle = f'Download: {download_speed}',
       message  = f'Upload: {upload_speed} Sever: {server_results}')