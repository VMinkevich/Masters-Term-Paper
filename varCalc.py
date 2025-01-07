import numpy as np
import scipy.stats as stats

class EnergyOptionRiskCalculator:
    def __init__(self, strike_price, spot_price, volatility, interest_rate, days_to_expiration, option_type="call", simulations=10000):
        """
        Инициализация калькулятора риска для опциона на электроэнергию.
        
        :param strike_price: Цена страйк опциона
        :param spot_price: Текущая цена базового актива (электроэнергии)
        :param volatility: Волатильность цены базового актива
        :param interest_rate: Процентная ставка (для дисконтирования)
        :param days_to_expiration: Количество дней до экспирации опциона
        :param option_type: Тип опциона ("call" или "put")
        :param simulations: Количество симуляций для метода Монте-Карло
        """
        self.strike_price = strike_price
        self.spot_price = spot_price
        self.volatility = volatility
        self.interest_rate = interest_rate
        self.days_to_expiration = days_to_expiration
        self.option_type = option_type
        self.simulations = simulations

    def simulate_price_paths(self):
        """
        Моделирование цен с помощью процесса геометрического броуновского движения.
        :return: Массив с результатами симуляций цен электроэнергии
        """
        dt = 1 / 252  # Один торговый день
        mu = self.interest_rate  # Средняя доходность (для простоты считаем, что равна процентной ставке)
        price_paths = np.zeros(self.simulations)
        
        # Моделируем цену на основе процесса Брауна
        for i in range(self.simulations):
            path = self.spot_price
            for t in range(self.days_to_expiration):
                path *= np.exp((mu - 0.5 * self.volatility**2) * dt + self.volatility * np.sqrt(dt) * np.random.normal())
            price_paths[i] = path
        
        return price_paths

    def calculate_option_payoffs(self, price_paths):
        """
        Рассчитываем выплаты по опциону.
        :param price_paths: Сценарии будущих цен
        :return: Массив с выплатами по опционам
        """
        if self.option_type == "call":
            payoffs = np.maximum(price_paths - self.strike_price, 0)
        elif self.option_type == "put":
            payoffs = np.maximum(self.strike_price - price_paths, 0)
        else:
            raise ValueError("Тип опциона должен быть 'call' или 'put'.")
        return payoffs

    def calculate_VaR(self, payoffs, confidence_level=0.95):
        """
        Рассчитываем VaR на основе исторических симуляций.
        :param payoffs: Массив выплат по опционам
        :param confidence_level: Уровень доверия (например, 0.95 для 95% доверительного интервала)
        :return: VaR
        """
        # Рассчитываем возможные убытки
        losses = np.maximum(self.strike_price - payoffs, 0)
        
        # Находим VaR как квантиль убытков
        var = np.percentile(losses, (1 - confidence_level) * 100)
        return var

    def calculate_CVaR(self, payoffs, confidence_level=0.95):
        """
        Рассчитываем CVaR (Conditional VaR) для заданного уровня доверия.
        :param payoffs: Массив выплат по опционам
        :param confidence_level: Уровень доверия (например, 0.95 для 95% доверительного интервала)
        :return: CVaR
        """
        # Рассчитываем возможные убытки
        losses = np.maximum(self.strike_price - payoffs, 0)
        
        # Находим VaR
        var = self.calculate_VaR(payoffs, confidence_level)
        
        # Рассчитываем CVaR как среднее значение потерь, которые больше чем VaR
        cvar = losses[losses >= var].mean()
        return cvar

    def calculate_risk_metrics(self):
        """
        Основная функция для расчёта VaR и CVaR.
        :return: Словарь с результатами VaR и CVaR
        """
        # Симулируем цены
        price_paths = self.simulate_price_paths()

        # Рассчитываем выплаты по опциону
        payoffs = self.calculate_option_payoffs(price_paths)

        # Рассчитываем VaR и CVaR
        var = self.calculate_VaR(payoffs)
        cvar = self.calculate_CVaR(payoffs)

        return {"VaR": var, "CVaR": cvar}

# Пример использования
if __name__ == "__main__":
    # Параметры опциона
    strike_price = 50  # Цена страйк опциона
    spot_price = 55    # Текущая цена базового актива (электроэнергия)
    volatility = 0.2   # Волатильность
    interest_rate = 0.03  # Процентная ставка
    days_to_expiration = 365  # Дни до экспирации опциона
    option_type = "call"  # Тип опциона (например, колл)
    
    # Создаём объект для расчёта VaR и CVaR
    option_risk_calculator = EnergyOptionRiskCalculator(
        strike_price=strike_price, 
        spot_price=spot_price, 
        volatility=volatility,
        interest_rate=interest_rate, 
        days_to_expiration=days_to_expiration,
        option_type=option_type, 
        simulations=10000
    )

    # Рассчитываем риски
    risk_metrics = option_risk_calculator.calculate_risk_metrics()

    print(f"VaR (95% confidence level): {risk_metrics['VaR']:.2f}")
    print(f"CVaR (95% confidence level): {risk_metrics['CVaR']:.2f}")
