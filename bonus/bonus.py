
#%%
contents = ["content1 - Vamos adicionar essas merdas do caralho", 'content2', 'content3']
filenames = ["test1", "test2", "test3"]

for content, filename in zip(contents, filenames):
    # Corrected the filename variable in the open statement
    with open(f"{filename}.txt", 'w') as file:
        file.write(content)

# %%
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    with open(f"{filename}.txt", 'w') as file:
        file.writelines('Hello')
# %%

filenames = ["1.doc", "1.report", "1.presentation"]
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)
# %%
