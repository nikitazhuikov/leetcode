class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        """
        maxDam = 0
        def spellList(power: list[int], maxDam: int) -> int:
            spell = []
            for i in range(len(power)):
                if power[i] + 1 not in spell and power[i] - 1 not in spell and power[i]+2 not in spell and power[i]-2 not in spell:
                    spell.append(power[i])
                if i == len(power):
                    maxDam = max(maxDam, sum(spell))
                    return maxDam
                spellList(power[i+1::], maxDam)

        spellList(power, maxDam)
        return maxDam
        """
        import bisect
        from collections import Counter
       # 1. Считаем частоту каждого заклинания
        count = Counter(power)
        # 2. Берем уникальные значения и сортируем их
        unique = sorted(count.keys())
        n = len(unique)
        
        # dp[i+1] хранит максимальный урон, который можно получить,
        # используя первые i+1 уникальных заклинаний.
        dp = [0] * (n + 1)
        
        for i in range(n):
            val = unique[i]
            # Урон, который мы получим, если возьмем все заклинания этого типа
            current_damage = val * count[val]
            
            # 3. Находим индекс j первого элемента, который НЕЛЬЗЯ брать (т.е. >= val - 2)
            # Все элементы с индексами меньше j (от 0 до j-1) — безопасны.
            # В бинарном поиске ищем val - 2.
            j = bisect.bisect_left(unique, val - 2)
            
            # 4. Выбираем максимум:
            # - Мы НЕ берем текущее заклинание: результат такой же, как dp[i]
            # - Мы БЕРЕМ текущее заклинание: прибавляем current_damage к dp[j] 
            # (где dp[j] — это накопленный максимум для безопасных элементов)
            dp[i+1] = max(dp[i], current_damage + dp[j])
            
        return dp[n]


if __name__ == "__main__":
    from collections import Counter
    solution = Solution()
    print(solution.maximumTotalDamage([2,2,3,5,7,8,9,9,10,10]))
    print(sorted([2,2,3,5,7,8,9,9,10,10]))
    print(Counter([2,2,3,5,7,8,9,9,10,10]))
