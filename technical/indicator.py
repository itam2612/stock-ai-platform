import pandas as pd
import ta


class IndicatorCalculator:

    @staticmethod
    def add_all(df):

        df = df.copy()

        close = df["Close"]
        high = df["High"]
        low = df["Low"]
        volume = df["Volume"]

        ####################################################
        # SMA
        ####################################################

        df["SMA5"] = ta.trend.sma_indicator(close,5)
        df["SMA25"] = ta.trend.sma_indicator(close,25)
        df["SMA75"] = ta.trend.sma_indicator(close,75)
        df["SMA200"] = ta.trend.sma_indicator(close,200)

        ####################################################
        # EMA
        ####################################################

        df["EMA12"] = ta.trend.ema_indicator(close,12)
        df["EMA26"] = ta.trend.ema_indicator(close,26)

        ####################################################
        # RSI
        ####################################################

        df["RSI"] = ta.momentum.rsi(close,14)

        ####################################################
        # MACD
        ####################################################

        macd = ta.trend.MACD(close)

        df["MACD"] = macd.macd()
        df["MACD_SIGNAL"] = macd.macd_signal()
        df["MACD_DIFF"] = macd.macd_diff()

        ####################################################
        # Bollinger
        ####################################################

        bb = ta.volatility.BollingerBands(close)

        df["BB_UPPER"] = bb.bollinger_hband()
        df["BB_MIDDLE"] = bb.bollinger_mavg()
        df["BB_LOWER"] = bb.bollinger_lband()
        df["BB_WIDTH"] = bb.bollinger_wband()

        ####################################################
        # ATR
        ####################################################

        df["ATR"] = ta.volatility.average_true_range(
            high,
            low,
            close
        )

        ####################################################
        # ADX
        ####################################################

        adx = ta.trend.ADXIndicator(
            high,
            low,
            close
        )

        df["ADX"] = adx.adx()

        ####################################################
        # Stochastic
        ####################################################

        st = ta.momentum.StochasticOscillator(
            high,
            low,
            close
        )

        df["STOCH"] = st.stoch()
        df["STOCH_SIGNAL"] = st.stoch_signal()

        ####################################################
        # CCI
        ####################################################

        df["CCI"] = ta.trend.cci(
            high,
            low,
            close
        )

        ####################################################
        # ROC
        ####################################################

        df["ROC"] = ta.momentum.roc(close)

        ####################################################
        # OBV
        ####################################################

        df["OBV"] = ta.volume.on_balance_volume(
            close,
            volume
        )

        ####################################################
        # 出来高平均
        ####################################################

        df["VOL20"] = volume.rolling(20).mean()

        ####################################################
        # 出来高倍率
        ####################################################

        df["VOL_RATIO"] = volume / df["VOL20"]

        ####################################################
        # 高値更新
        ####################################################

        df["HIGH20"] = high.rolling(20).max()

        ####################################################
        # 安値更新
        ####################################################

        df["LOW20"] = low.rolling(20).min()

        return df