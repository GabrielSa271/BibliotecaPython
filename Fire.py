import fire

class Calculator:
    """Classe simples de calculadora"""
    
    def add(self, x, y):
        """Soma dois números"""
        return x + y

    def multiply(self, x, y):
        """Multiplica dois números"""
        return x * y

if __name__ == '__main__':
    fire.Fire(Calculator)

