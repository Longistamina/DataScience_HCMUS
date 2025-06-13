# XML = eXtensible Markup Language
# It is designed for facilitating data transfering and storing
# Main purpose: simplify the data sharing process between systems, especially via Internet 

# XML file has a tree-like structure

#------------------------------------------------#
#-------------- XML file structure --------------#
#------------------------------------------------#

# <?xml version="1.0" encoding="UTF-8"?>    (This line tells the computer that we are using XML, the content version is 1.0, with UTF-8 encoding)

# <CATALOG>   (This is the start of the Root Element. Each XML file has ONLY ONE Root Element)

#   <CD>      (This is the start of a Child Element. Each Child Element can also have their own Child Elements. But should not > 3 levels)

#     <TITLE>Empire Burlesque</TITLE>   (This is the Child Element of element <CD>, which is also a child element itself)

#     <ARTIST>Bob Dylan</ARTIST>

#     <COUNTRY>USA</COUNTRY>

#     <COMPANY>Columbia</COMPANY>

#     <PRICE>10.90</PRICE>

#     <YEAR>1985</YEAR>

#   </CD>

# </CATALOG> (This is the end of the Root Element. Agian, each XML file has ONLY ONE Root Element)

## Start an element: <element_name>
##                      contents ......................
##                      contents ......................
##                      contents ......................
## End an element:   </element_name>

## Element can also be called as "Node"

## The Element/Node level should not exceed 3
##     <Root_Element>
##      <Child_Element_Level_1>
##       <Child_Element_Level_2>
##        <Child_Element_Level_3>


########################### Install XML library ######################

# install.packages("XML")
# conda install -c conda-forge r-xml


#---------------------------------------------------------------------#
#------------------- read XML file into R dataframe ------------------#
#---------------------------------------------------------------------#

# install.packages("XML")
# conda install -c conda-forge r-xml

library("XML")
library("methods")

# use xmlToDataFrame() to read a .xml file into a dataframe
df_cd <- xmlToDataFrame("data_chap_10/demo_data/cd.xml")
head(df_cd)
print(class(df_cd))


#----------------------------------------------------------------------#
#------------------- save R dataframe into .xml file ------------------#
#----------------------------------------------------------------------#

# create new cd dataframe with country USA only
df_cd_usa = df_cd[df_cd["COUNTRY"] == "USA", ]
head(df_cd_usa)

################### Create XMLDoc() Object to store data of a dataframe #############################
# XML library's commands can only save XML object
# Therefore, must convert our dataframe into XML object first, using newXMLDoc() and newXMLNode()

library("XML")

# creates a new internal XML document object in R that serves as the foundation for building XML trees
xmldoc_cd_usa <- newXMLDoc() 

# create the root_node named "CATALOG" for the xmldoc_cd_usa object
root_node <- newXMLNode(name = "CATALOG", doc = xmldoc_cd_usa) 

# Loop through each record (row) of the df_cd_usa
for (record in 1:nrow(df_cd_usa)) {
    # At the beginning of each record, create a child_node_lv1 named "CD" that takes root_node as parent
    child_node_lv1 = newXMLNode(name = "CD", parent = root_node) 
    
    # Loop through each field (column) of each record
    for (field in colnames(df_cd_usa)) { 
        # Create each child_node_lv2 that represents each field that takes "CD" child_node_lv2 as parent
        newXMLNode(name = field, df_cd_usa[record, field], parent = child_node_lv1)  
    }
}

############################# Save XMLDoc object into .xml file ####################
# use cat(saveXML(....), file = "path/to/save/file") to save a dataframe into a .xml file

cat(
    saveXML(
        doc = xmldoc_cd_usa, # XMLDoc object to be saved
        indent = TRUE,       # set indent = TRUE so that the childe node will be indented every level
        prefix = '<?xml version="1.0" encoding="UTF-8"?>standalone=\"no\"?>\n'         
        # prefix is a string that is written to the stream/connection at the beginning of the xml file, before the XML is output.
    ),
    file = "data_chap_10/demo_data/cd_usa_xmldoc_from_df.xml"
)
