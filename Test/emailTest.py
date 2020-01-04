from sparkpost import SparkPost

sp = SparkPost('952b3fd41adb013f97e54ed4e0d861341e460d03')

response = sp.transmissions.send(
    use_sandbox=True,
    recipients=['shubhamtiwaricr07@gmail.com'],
    html='<p>Hello world</p>',
    from_email='no-reply@sparkpostbox.com',
    subject='Hello from python-sparkpost'
)

print(response)
