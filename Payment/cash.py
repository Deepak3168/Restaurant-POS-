from .service import PaymentService


class CashPayment(PaymentService): 

    def __init__(self,order,cash_recieved=0) : 
        self.__cash_recieved = cash_recieved 
        self.order = order
        self.__payment_status = False

    def process_payment(self):
        if self.__cash_recieved >= self.order.calculate_sub_total() : 
            self.__payment_status = True 
            return True
        else:
            return False


    def caliculate_change(self):
        return self.__cash_recieved - self.order.caliculate_subtotal()

    def set_cash_recieved(self,cash_recieved):
        self.__cash_recieved = cash_recieved 
        
        
    

    

    

        
