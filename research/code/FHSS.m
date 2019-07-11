% Lab 06
% WiCom_4
% By Kashif Shahzad 
% 01-ET-31
% 4th July 2004

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CDMA coding and decoding mechanism
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc
clear

% Generation of Random Bits
r=round(rand(1,20));

% Chip Pattern for station A, B and C
a_one=[1 -1 -1 1 -1 1];
a_zero=-1*a_one;
b_one=[1 1 -1 -1 1 1];
b_zero=-1*b_one;
c_one=[1 1 -1 1 1 -1];
c_zero=-1*c_one;

% Random Allotment of bits to stations A,B and C
cdma_seq=[];
for counter=1:20
    switch(rand(1,1,[1 3]))
        case(1)
            if r(1,counter)==0;
                cdma_seq=[cdma_seq a_zero];
            else
                cdma_seq=[cdma_seq a_one];
            end
        case(2)
            if r(1,counter)==0;
                cdma_seq=[cdma_seq b_zero];
            else
                cdma_seq=[cdma_seq b_one];
            end
        case(3)
            if r(1,counter)==0;
                cdma_seq=[cdma_seq c_zero];
            else
                cdma_seq=[cdma_seq c_one];
            end
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   Decoding the Signal
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
cntr=0;
for selector=1:6:120
    cntr=cntr+1;
    temp=[cdma_seq(1,selector) cdma_seq(1,selector+1) cdma_seq(1,selector+2) ...
            cdma_seq(1,selector+3) cdma_seq(1,selector+4) cdma_seq(1,selector+5)];
    result1=dot(a_one,temp);
    result2=dot(b_one,temp);
    result3=dot(c_one,temp);
    if (result1==6)|(result1==-6)
        fprintf('\nThe bit # %d is from Station A',cntr);
    else 
        if (result2==6)|(result2==-6)
            fprintf('\nThe bit # %d is from Station B',cntr);
        else
            if (result3==6)|(result3==-6)
                fprintf('\nThe bit # %d is from Station C',cntr);
            end
        end
    end
end