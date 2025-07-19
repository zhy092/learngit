import akshare as ak
import pandas as pd

# 股票分析核心模块（支持实时数据获取和技术分析）
class StockAnalyzer:
    def get_realtime_data(self):
        """使用AKShare获取实时股票数据<mcreference link="https://akshare.akfamily.xyz/index.html" index="1">1</mcreference>"""
        return ak.stock_zh_a_spot()

    def calculate_moving_average(self, days=5):
        """计算移动平均线
        
        Args:
            days (int): 移动平均周期
        """
        hist_data = ak.stock_zh_a_daily(symbol=self.symbol)
        return hist_data['close'].rolling(window=days).mean()

if __name__ == "__main__":
    analyzer = StockAnalyzer("sh600000")
    print("实时行情：\n", analyzer.get_realtime_data().head())
    print("5日均线：\n", analyzer.calculate_moving_average())