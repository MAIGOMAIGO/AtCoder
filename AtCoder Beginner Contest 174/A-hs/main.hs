toInt::(String -> Int)
toInt x = read x::Int
which::(Int -> String)
which w = if w>=30 then "Yes" else "No"
main = do
  x <- getLine
  let s = toInt x
  putStr $ which s
