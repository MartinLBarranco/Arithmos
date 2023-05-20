module Main where

main :: IO()
main = do
    linea <- readFile "datos.txt"
    let res = show (calculaFactorial linea)
    writeFile "resultado.txt" res

factorial :: Integer -> Integer
factorial n = foldr (*) 1 [1..n]

calculaFactorial :: String -> Integer
calculaFactorial xs = factorial (read xs)