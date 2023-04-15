from os import listdir
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.document_loaders import UnstructuredMarkdownLoader

def load_file(ref):
    files = [ref['file']]
    if ref["folder"]:
        files = listdir('content/'+ref["file"])
        for j in range(len(files)):
            files[j] = ref["file"]+'/'+files[j]

    for file in files: 
        path = "content/"+file
        print(path)
        if ref["fileType"] == "pdf":
            loader = UnstructuredPDFLoader(path)
        elif ref["fileType"] == "md":
            loader = UnstructuredMarkdownLoader(path)
        else:
            print("File type not supported")

        try:
            document = loader.load()
            document[0].metadata = ref
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            documents = text_splitter.split_documents(document)
            return documents
        except Exception as e:
            print(e)
            print("Error loading file")