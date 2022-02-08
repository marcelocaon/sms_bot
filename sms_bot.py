# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

nome, celular, mensagem = '', '', ''
num, razao_social, valor = '','',''

def enviar_sms(msg, to_ven):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACe70c373c58f6436d1c1486d6e41ab9c2'
    auth_token = '3acace0c78f26a413bdf58b545b7be91'
    client = Client(account_sid, auth_token)
    #print("ENTROU NO ENVIAR_SMS()")
    print("TO: ",to_ven)
    #message = client.messages \
    #.create(
    message = client.messages.create(
        body=msg,
        from_='+5534933007290',
        status_callback='http://postb.in/1234abcd',
        #to='+5548985052905'
        to=to_ven
     )
    #print("msg = ",msg)
    #print("to = ",to)
    #print(message.sid)
    
def enviar(c):
    for lista in c:
        nome = lista[0]
        #print(nome)
        pedido = lista[1]
        #print(pedido)
        razao_social = lista[2]
        #print(razao_social)
        fantasia = lista[3]
        #print(fantasia)
        valor = lista[4]
        #print(valor)
    
        mensagem= f'Recebido pedido numero: {pedido} do cliente: {razao_social} no valor de RS {valor}'
        print(f'Tentativa de envio de SMS: {nome}')
        print(mensagem)

        try:
            if nome == 2:
                #telefone da rose
                to_ven='+5548991409851'
            elif nome == 30:
                #telefone do adenor
                to_ven='+5548991430433'
            elif nome == 39:
                #telefone do vagner
                to_ven='+5548991103693'
            elif nome == 45:
                #telefone do aldi
                to_ven= '5548991805281'
                
            enviar_sms(mensagem, to_ven)
        except:
            print('Não foi possível enviar sms para o vendedor ' + str(nome) + 'do pedido numero: '+str(pedido))


