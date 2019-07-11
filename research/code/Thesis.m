classdef Thesis < handle
   properties
      saveFigures=true
      savedFigures=[]
      figureFileType=".png"
   end
   methods(Static)

   end
   methods      
       function saveFiguresPrompt(obj,default)
           if ~exist('default','var')
               default = "N";
           end
           figureSave = input(char(strcat("Do you want to save figures? Y/N [",default,"]:")),'s');
           obj.saveFigures = strcmp(figureSave,'Y');
       end
       
       function saveFigure(obj, f,filename)
           figureRoot='../../figures/';
           if obj.saveFigures == true
               if (exist(figureRoot,'dir') == 0)
                   mkdir(figureRoot)
               end
               filepath = char(lower(strcat(figureRoot,filename,obj.figureFileType)));
               saveas(f,filepath);
               obj.savedFigures=[obj.savedFigures,filepath];
           end
       end      
   end
end