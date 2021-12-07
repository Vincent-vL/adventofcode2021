p = table2array(readtable('input7.txt'));
a = min(p);
b = max(p);
mincost = inf;
minvalue = 0;
for i=a:b
   n = abs(p-i);
   cost = sum(n.*(n+1)./2); % gaussian summation
   if cost < mincost
       mincost = cost;
       minvalue = i;
   end
end

mincost
minvalue
