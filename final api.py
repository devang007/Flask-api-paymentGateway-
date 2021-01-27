#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


from flask import Flask, request, render_template 
import random

app = Flask(__name__, template_folder="templates")

@app.route('/')
def my_form():
    return render_template('temp.html')


class CheapPaymentGateway:
    
    def cheappayment():
        
        state=random.randint(0,1)
        if state==1:
           
            return "payment success (CheapPaymentGateway)"
            
            
        else:
            return "CheapPayment gateway busy"
class ExpensivePaymentGateway:
    
    def expensivepayment():
       
        state=random.randint(0,1)
        if state==1:
         
            return "payment success (ExpensivePaymentGateway)"
        else:
            print("Retrying with CheapPaymentGateway(expensive)")
            CheapPaymentGateway.cheappayment()

class PremiumPaymentGateway:
    
    def premiumpayment():
        
        state=random.randint(0,1)
        if state==1:
            
            return "payment success (PremiumPaymentGateway)"
        elif 1:
            refresh=1
            
            if refresh < 4:
                refresh=refresh+1
                PremiumPaymentGateway.premiumpayment()
            else:
                return "PremiumPaymentGateway busy"
       
               




@app.route('/', methods=['POST'])

def ProcessPayment():
    amount= request.form['amt']
    amount=int(amount)
    
    refresh=0
    if amount > 500:
        
        status=PremiumPaymentGateway.premiumpayment()
    elif 20 < amount <=500:
        
        status=ExpensivePaymentGateway.expensivepayment()
    else:
        
        status=CheapPaymentGateway.cheappayment()
    return status
    
    
       
    
    

if __name__ == '__main__':
    app.run(debug=False)


# In[ ]:





# In[ ]:





# In[ ]:




