p = table2array(readtable('input7.txt'));
a = min(p);
b = max(p);
k = size(p,2);
m = k*(b-a);
for i=a:b
   cost = sum(abs(p-i));
   if cost < m
       m = cost;
   end
end

m
