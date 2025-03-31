from flask import Flask,render_template,request,jsonify
from twilio.rest import Client
app=Flask(__name__)
account_sid='حساب_sid_خود'
auth_token='توکن_احراز_هویت_خود'
twilio_phone_number='09399815417'
Client=Client(account_sid,auth_token)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/send-message',methods=['post'])
def send_message():
    date=request.json
    phone_number=date.get('phone_number')
    message=date.get('message')
    if phone_number and message:
        try:
            send_message=Client.messages.create(
                body=message,
                from_=twilio_phone_number,
                to=phone_number
            )
            return jsonify({'status':'success','message':'Message sent!','sid':message.sid}),200
        except Exception as e:
            return jsonify({'status':'error','message':'Error Sending Message!','error':str(e)}),500
    return jsonify({'status':'error','message':'The information is incomplete!'}),400
if __name__=='__main__':
    app.run(debug=True)