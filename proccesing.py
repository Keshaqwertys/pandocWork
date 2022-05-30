import sys
import panflute

headersList = list()


def filtrationProcess(element, doc):
    if isinstance(element, panflute.Header):
        string = panflute.stringify(element)
        if string in headersList:
            sys.stderr.write("Repeated header: " + string + "\n")
        else:
            headersList.append(string)
    if isinstance(element, panflute.Str) and element.text.lower() == "bold":
        return panflute.Strong(element)
    if isinstance(element, panflute.Header) and element.level <= 3:
        return element.walk(upperStr)


def upperStr(element, doc):
    if isinstance(element, panflute.Str):
        element.text = element.text.upper()


def main(doc=None):
    return panflute.run_filter(filtrationProcess, doc=doc)


if __name__ == "__main__":
    main()
