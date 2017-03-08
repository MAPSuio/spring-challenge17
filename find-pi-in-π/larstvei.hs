import Prelude hiding (pi)
import Data.List (isPrefixOf)

needle = [2,0,5,5,3]

pi = g(1,0,1,1,3,3)
    where g(q,r,t,k,n,l) =
              if 4*q+r-t<n*t
              then n : g(10*q,10*(r-n*t),t,k,div(10*(3*q+r))t-10*n,l)
              else g(q*k,(2*q+r)*l,t*l,k+1,div(q*(7*k+2)+r*l)(t*l),l+2)

findIndexOf x (y:ys) | x `isPrefixOf` (y:ys) = 0
                     | otherwise = 1 + findIndexOf x ys

main = print $ findIndexOf needle pi
