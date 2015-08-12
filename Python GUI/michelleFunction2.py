from Tkinter import *

tutorialString = "1.\tNavigate to the folder where the data is stored. The files should appear under current folder.\r\n2.\tFind the file you hope to plot and double-click the mat file.\r\n\t>> load('Sand_60_1_070915') will show up in the command window. \r\n\tDouble-clicking the file is equivalent to typing the above command. After loading the file, all variables in this\r\n\tmat file will be displayed in the workspace as they are added to your current workspace. (If a new variable has\r\n\tthe same name of a variable that already exists in the workspace, the old one will be overwritten.)\r\n3.\tIn the files we work with, the variable \"out\" always stores the spectra in a matrix with the dimension of 182401\r\n\tby 10. (182401 is the number of data points in each spectrum, and we have 10 spectra because there are 5\r\n\truns, each including two scans.)\r\n\t\ta.\tresult1 = out(:,1); stores the first spectrum out of the 10 in a variable called result1. The colon inside the \r\n\t\t\tparenthesis represents the entire column, and 1 indicates the first element of a row. Together result1 = \r\n\t\t\tout(:,1) means taking the first column of the variable out and assigning it to a variable called result1.\r\n\t\tb.\tresult2 =mean(out')'; averages all the spectra and stores the resulting spectrum in the variable result2. \r\n\t\t\tThe apostrophe is an operator to transpose the matrix, changing an m*n matrix to an n*m matrix. We first \r\n\t\t\ttranspose the matrix so that we can take the average of the spectra and then we transpose it back to \r\n\t\t\tpreserve its shape (that's why there're two apostrophes). This practice is preferred, but it's slightly slower \r\n\t\t\tthan (a).\r\n4.\tIf another file needs to be loaded, simply double-click that mat file under current folder. All variables including\r\n\t\"out\" will be overwritten except those that don't exist in this new mat file like result1 and result2 we just\r\n\tcreated. Now repeat step 3 but assign different variable names like result3 = mean(out')'; so that we can store\r\n\tthe spectrum information in the file we just loaded. \r\n5.\tThe commend plot(wave, result1) will plot the graph for you. Wave is the variable on the x-axis, and results1 is\r\n\tthe variable on the y-axis. If two spectra need to be plotted in the same graph, the command should be\r\n\tplot(wave, result1, wave, result2)\r\n6.\tWe can also add legend and labels to make the graph prettier. plot(wave, result1, wave, result3);\r\n\tlegend(\'60ml\/dl\',\'100ml\/`dl\'); xlabel(\'wavenumber cm^{-1}\'); ylabel(\'signal (a.u.)\')\r\n\tThe graph is editable after it's been plotted. For example, you can drag the legend to wherever you want,\r\n\tchange its shape or color, add a title for the graph, etc.\r\n7.\tSave the graph in the format in pdf or jpg is convenient. The fig format is also recommended because the\r\n\tgraph can be edited later (it can only opened in MATLAB though).\r\n\r\nA few remarks:\r\n1.\tPutting a semicolon after each command is important because it suppresses the output and prevents the\r\n\tprogram from printing out everything in the command window. \r\n2.\tYou can get help by typing \"help\" in the command window. For example \"help plot\" can show you all\r\n\tinformation about the plot function.\r\n3.\tTo stop executing a command in the middle of a test, press Ctrl+C. On a Mac, use Command+. (the\r\n\tCommand key and the period key)."
 
root = Tk()
root.columnconfigure(0, weight=1)
text = Text(root, width = 136)
text.grid()
text.insert(END, tutorialString)
scrl = Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scrl.set)
scrl.grid(row=0, column=1, sticky='ns')
root.mainloop()