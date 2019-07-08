from lxml import etree
import re
import fasttext
import unidecode


def XML_to_text(path):
    """
    Get main text from xml file
    :param path: path to the file to transform
    :return: a tuple with auts, and string (the text).
    """

    myxsl = etree.XML('''
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="1.0">
    
    <xsl:output method="text"/>
    
    <xsl:template match="/">
        <xsl:apply-templates
            select="song/text"/>
    </xsl:template>
    
</xsl:stylesheet>''')
    myxsl = etree.XSLT(myxsl)

    with open(path, 'r') as f:
        my_doc = etree.parse(f)

        auts = my_doc.findall("//author")
        auts = [a.text for a in auts]

        if not len(auts) == 1:
            print("Error: more or less than one author in" + path)

            if len(auts) == 0:
                auts = [None]

        if auts == [None]:
            aut = "unknown"

        else:
            aut = auts[0]

        return aut, re.sub(r"\s+", " ", str(myxsl(my_doc)))


def identify_lang(string, model):
    """
    Get the language from a string
    :param string: a string, duh
    :param model, the fasttext model
    :return: the language
    """

    return model.predict(string)  # , k = 3)


def normalise(text):
    # Remove all but word chars, remove accents, and normalise space
    # and then normalise unicode

    return unidecode.unidecode(re.sub(r"\s+", " ", re.sub(r"[\W0-9]+", " ", text.lower()).strip()))


def load_texts(paths, fasttext_model):
    """
    Loads a collection of documents into a 'myTexts' object for further processing.
    TODO: a proper class
    :param paths: path to docs
    :param fasttext_model: model for language identification
    :return: a myTexts object
    """

    myTexts = []
    # langCerts = []

    for path in paths:
        name = path.split('/')[-1]
        aut, text = XML_to_text(path)
        lang, cert = identify_lang(text, fasttext_model)
        lang = lang[0].replace("__label__", "")

        # Normalise text once and for all
        text = normalise(text)

        myTexts.append({"name": name, "aut": aut, "text": text, "lang": lang})

        # if cert < 1:
        # langCerts.append((lang, name, cert))

        # directory = "train_txt/" + lang + "/" + aut + "/"

        # if not os.path.exists(directory):
        #    os.makedirs(directory)

        # with open(directory + name + ".txt", "w") as out:
        #    out.write(text)

    # with open("lang_certs.csv", 'w') as out:
    #    for line in langCerts:
    #        out.write("{}\t{}\t{}\t\n".format(line[0], line[1], float(line[2])))
    return myTexts