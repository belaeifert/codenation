from calendar import monthrange
from datetime import date


class CloudCost():

    def lambda_execution(self):
        '''
        Calculates the value one function in the cloud

        :return: The cost of one function in cloud
        '''
        function_execution_value = 0.0000002
        execution_time_value = 0.0002080

        return ((function_execution_value) + (execution_time_value * 3))

    def app_execution(self, execution_times):
        '''
        Calculates the cost of N requests in the cloud

        :param execution_times: Quantity of requests made to cloud
        :return: The total cost of N request to cloud
        '''
        message_in_line_value = 0.00000040
        return execution_times * (message_in_line_value + (self.lambda_execution() * 2))


    def month(self, execution_times, month_of_year):
        '''
        Calculates the monthly cost of N requests in the cloud

        :param execution_times: Quantity of requests made to cloud
        :param month_of_year: Month's number used to calculate the cost
        :return: The total cost of N request to cloud in a month
        '''
        return monthrange(date.today().year, month_of_year)[-1] * self.app_execution(execution_times)
    
    def year(self, execution_times):
        '''
        Calculates the annual cost of N requests in the cloud
        :param execution_times: Quantity of requests made to cloud
        :return: The total cost of N request to cloud in a year
        '''
        return [self.month(execution_times, month_of_year) for month_of_year in range(1, 13)] + [self.month(execution_times, 4)]
        # return [self.month(execution_times, month_of_year) for month_of_year in range(1, 13)]


if __name__ == '__main__':
    cc = CloudCost()
    print(cc.app_execution(1))
'''
    meu = cc.year(1)
    resposta = [0.0387128, 0.0349664, 0.0387128, 0.037464, 0.0387128, 0.037464, 0.0387128, 0.0387128, 0.037464,  0.0387128, 0.037464, 0.0387128, 0.037464]
    print(resposta == meu)
    print(resposta)
    print(meu)
'''



