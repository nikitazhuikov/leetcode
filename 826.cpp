class Solution {
    public:
        int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
            int n = difficulty.size();
            int m = worker.size();
            
            // Создаем пары (сложность, прибыль)
            vector<pair<int, int>> jobs;
            for (int i = 0; i < n; i++) {
                jobs.push_back({difficulty[i], profit[i]});
            }
            
            // Сортируем задания по сложности
            sort(jobs.begin(), jobs.end());
            
            // Сортируем работников по способностям
            sort(worker.begin(), worker.end());
            
            int totalProfit = 0;
            int maxProfit = 0;  // Максимальная прибыль среди доступных заданий
            int jobIndex = 0;
            
            // Для каждого работника находим максимальную прибыль
            for (int i = 0; i < m; i++) {
                // Проходим по всем заданиям, которые может выполнить текущий работник
                while (jobIndex < n && jobs[jobIndex].first <= worker[i]) {
                    maxProfit = max(maxProfit, jobs[jobIndex].second);
                    jobIndex++;
                }
                
                // Назначаем работнику лучшее доступное задание
                totalProfit += maxProfit;
            }
            
            return totalProfit;
        }
    };