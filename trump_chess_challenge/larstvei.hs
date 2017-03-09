-- A brute force solution to The Trump Challenge
import Data.List ((\\), subsequences)

ratings = [2838.0, 2822.0, 2817.0, 2811.0, 2803.0, 2793.0, 2786.0, 2783.0, 2774.0, 2772.0, 2771.3, 2761.0, 2759.0, 2755.1, 2751.1, 2751.0, 2750.0, 2749.6, 2746.8, 2745.0, 2741.0, 2739.0, 2734.0, 2732.0, 2728.6]

avg xs = sum xs / (fromIntegral $ length xs)

counterTournament t = take 2 $ ratings \\ t

winning xs = length xs > 1 && (length ct < 2 || avg xs > avg ct)
    where ct = counterTournament xs

main = print $ length $ filter winning $ subsequences ratings
