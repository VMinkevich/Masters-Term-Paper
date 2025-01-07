Для расчёта **Value at Risk (VaR)** и **Conditional Value at Risk (CVaR)** на **опционе на электроэнергию** можно использовать методы, основанные на **монте-карло моделировании** и **нормальном распределении** доходности.

### Что такое VaR и CVaR?

- **VaR (Value at Risk)** — это статистическая мера, которая оценивает потенциальные убытки на заданном уровне вероятности за определённый период. Это максимальный убыток, который не будет превышен с заданной вероятностью.
- **CVaR (Conditional Value at Risk)** — это средний убыток в условиях, когда убытки превышают уровень VaR. CVaR также называется **Expected Shortfall**.

В нашем примере, мы будем рассчитывать VaR и CVaR для опционного контракта на электроэнергию, используя **монте-карло моделирование** для оценки ценовых движений.

### Входные данные:
1. **Ставка страйк** (Strike price) для опциона.
2. **Цена базового актива** (например, цена электроэнергии).
3. **Волатильность** — стандартное отклонение изменений цены.
4. **Процентная ставка** (для дисконтирования).
5. **Количество дней до экспирации** опциона.
6. **Количество симуляций** для метода Монте-Карло.
7. **Тип опциона** (колл или пут).

### Алгоритм:
1. Генерируем случайные изменения цен электроэнергии с помощью нормального распределения.
2. Рассчитываем итоговую цену опциона для каждого из сценариев.
3. Находим **VaR** как квантиль убытков, соответствующий заданному уровню доверия.
4. Рассчитываем **CVaR** как средний убыток, который превышает **VaR**.


### Пояснение к коду:

1. **Генерация цен с помощью геометрического броуновского движения**:
   Мы используем модель геометрического броуновского движения для симуляции цен электроэнергии. В основе этого лежит следующее уравнение:
   \[
   S(t) = S(0) \cdot \exp\left( \left(\mu - \frac{1}{2} \sigma^2\right) t + \sigma \cdot \sqrt{t} \cdot Z \right)
   \]
   где:
   - \( S(t) \) — цена в момент времени \( t \),
   - \( \mu \) — средний доход,
   - \( \sigma \) — волатильность,
   - \( Z \) — случайная величина, распределённая нормально.

2. **Типы опционов**:
   В классе поддерживаются два типа опционов: **call** (колл) и **put** (пут). Для расчёта выплат по опциону используется стандартная формула для этих типов:
   - Для **call** опциона: \( \text{payoff} = \max(S_T - K, 0) \),
   - Для **put** опциона: \( \text{payoff} = \max(K -

 S_T, 0) \),
   где \( S_T \) — конечная цена, а \( K \) — цена страйк.

3. **Расчёт VaR и CVaR**:
   - **VaR** вычисляется как **квантиль** (percentile) на уровне доверия, обычно 95% или 99%.
   - **CVaR** вычисляется как **средний убыток** среди тех случаев, когда убытки превышают VaR.

### Пример работы:

Для примера, если у вас есть колл-опцион на электроэнергию с ценой страйк 50 и текущей ценой 55, с волатильностью 20% и процентной ставкой 3%, то этот класс выполнит расчёт VaR и CVaR для выбранного опциона.

### Заключение:

Этот класс позволяет рассчитывать **VaR** и **CVaR** для опциона на электроэнергию, используя моделирование Монте-Карло и геометрическое броуновское движение для оценки ценовых путей. Вы можете адаптировать его для других типов финансовых инструментов, добавив дополнительные параметры и улучшения.