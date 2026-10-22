from .service import PaymentService 


class UPIPayment(PaymentService):

    def __init__(self,upi_id,order,ref_id=None,):
        self.upi_id=upi_id 
        self.order = order 
        self.__payment_status 

    def process_payment(self):
        self.__payment_status = True
        return "UPI Payment Done"



