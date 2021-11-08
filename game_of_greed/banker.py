class Banker:
    """
    This class will handle the process of points during gameplay that when the user wants to save the points in bank or put it on the shelf
    """
    def __init__(self):
       self.balance=0
       self.shelved =0
        
    def shelf(self, points):
        """
        This method is to store the points on the shelf
        """
        self.shelved += points
        return self.shelved

        
    def bank(self):
        """
        This method is to send the points from shelf and store it in the bank
        """
        sender=  self.shelved
        self.shelved=0
        self.balance+=sender
        return self.balance

       
    def clear_shelf(self):
        """
        This method is to Clear the points from shelf
        """
       
        self.shelved=0
      
        return self.shelved
