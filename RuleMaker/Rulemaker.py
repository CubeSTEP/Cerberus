#!/bin/env python3

# -----------------------------------------------------------------------------------------------------------------------
# Rulemaker.py
#
# Generates and/or appends Rules declarations and definitions to the file test/ut/MyRules.hpp and test/ut/MyRules.cpp
# In addition, generates test/ut/RulesHeaders.hpp if the file does not already exist.
#
# Example:
#    ./Rulemaker <Rule Name>
#
# -----------------------------------------------------------------------------------------------------------------------

from Cheetah.Template import Template
from pathlib import Path
import argparse
import sys
import json


# -------------------------------------------------------------------------------------------------------------------------
# rulesHeaders
#
# Encapsulates the template for RulesHeaders.hpp
#
# Inputs:
#
# Returns:
#    The string of the declaration
# 
# -------------------------------------------------------------------------------------------------------------------------
def rulesHeaders():

    template = Template(r"""
#ifndef __RULES_HEADERS__
#define __RULES_HEADERS__

\#include "STest/STest/Rule/Rule.hpp"
\#include "STest/Scenario/BoundedScenario.hpp"
\#include "STest/Scenario/RandomScenario.hpp"
\#include "STest/Scenario/Scenario.hpp"

#endif""")

    return(str(template))


# -------------------------------------------------------------------------------------------------------------------------
# headerFile
#
# Encapsulates the template for a Rule class declaration
#
# Inputs:
#   RuleName :  The name of the Rule
#   ClassName:  The name of the class
#   ns       :  The namespace of the class
#
# Returns:
#    The string of the declaration
# 
# -------------------------------------------------------------------------------------------------------------------------
def headerFile(RuleName, ClassName, ns):

    template = Template(r"""
    
// ------------------------------------------------------------------------------------------------------
// Rule:  ${RuleName}
//
// ------------------------------------------------------------------------------------------------------
struct ${RuleName} : public STest::Rule<${ns}::${ClassName}>{
    // ----------------------------------------------------------------------
    // Construction
    // ----------------------------------------------------------------------

    //! Constructor
    ${RuleName}();

    // ----------------------------------------------------------------------
    // Public member functions
    // ----------------------------------------------------------------------

    //! Precondition
    bool precondition(
        const ${ns}::${ClassName}& state //!< The test state
    );

    //! Action
    void action(
        ${ns}::${ClassName}& state //!< The test state
    );
};""")

    template.RuleName = RuleName
    template.ClassName = ClassName
    template.ns = ns
    return(str(template))


# -------------------------------------------------------------------------------------------------------------------------
# implFile
#
# Encapsulates the template for a Rule class definition
#
# Inputs:
#   RuleName :  The name of the Rule
#   ClassName:  The name of the class
#   ns       :  The namespace of Tester
#
# Returns:
#    The string of the definition
#
# The first time this is used, add
# \#include "Tester.hpp" in the template
# 
# -------------------------------------------------------------------------------------------------------------------------
def implFile(RuleName, ClassName, ns, includeTheHeader):

    template = Template(r"""
    #if $includeTheHeader
\#include "${ClassName}.hpp"
    #end if

// ------------------------------------------------------------------------------------------------------
// Rule:  ${RuleName}
//
// ------------------------------------------------------------------------------------------------------
  
${ns}::${ClassName}::${RuleName}::${RuleName}() : STest::Rule<${ns}::${ClassName}>("${RuleName}"){}
    bool ${ns}::${ClassName}::${RuleName}::precondition(
        const ${ns}::${ClassName}& state //!< The test state
    ){
        return true;
    }
    
    void ${ns}::${ClassName}::${RuleName}::action(
        ${ns}::${ClassName}& state //!< The test state
    ){
        printf("--> Rule: %s \n", this->getName());
    }""")

    template.RuleName = RuleName
    template.ClassName = ClassName
    template.ns = ns
    template.includeTheHeader = includeTheHeader

    return(str(template))


# -------------------------------------------------------------------------------------------------------------------------
# Main routine
# -------------------------------------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description = "Unit Test Rule Generator.")
parser.add_argument("Rule", help = "The name of the rule")
#parser.add_argument("SetRuleSettings", help = "Set the namespace and class name of the file")

#subparsers = parser.add_subparsers(dest = "SetRuleSettings", help = "Available settings")

#settingsParser = subparsers.add_parser("a", help = "a")
parser.add_argument("-ns", "--Namespace", help = "The namespace of the class")
parser.add_argument("-cn", "--ClassName", help = "The name of the class")


args = parser.parse_args()

rule = args.Rule
ns = args.Namespace
ClassName = args.ClassName

rulesHFile = "MyRules.hpp"
rulesCFile = "MyRules.cpp"
rulesHeaderFile = "RulesHeaders.hpp"

#if (args.SetRuleSettings == "SetRuleSettings"):
    #print("hello")

SettingsFile = Path("RuleSettings.json")
SettingsNamespace = None
SettingsClassName = None

if (SettingsFile.is_file()):
    try:
        with open("RuleSettings.json") as File:
            Contents = json.load(File)

            SettingsNamespace = Contents["Namespace"]
            SettingsClassName = Contents["Class Name"]

            File.close()
    except json.JSONDecodeError:
        print("Invalid RuleSettings.json format")
    
    if (ns == None):
        ns = SettingsNamespace
    
    if (ClassName == None):
        ClassName = SettingsClassName
else:
    if ((ns == None) and (ClassName == None)):
        print("Misssing arguments: namespace and class name not defined. Run with -ns and -cn flags to specify namespace and class name respectively")

        sys.exit(0)
    elif (ns == None):
        print("Misssing argument: namespace not defined. Run with -ns flag to specify namespace")

        sys.exit(0)
    elif (ClassName == None):
        print("Misssing argument: class name not defined. Run with -cn flag to specify class name")

        sys.exit(0)

SettingsJSON = {
    "Namespace": ns,
    "Class Name": ClassName
}

JSONString = json.dumps(SettingsJSON)

with open("RuleSettings.json", "w") as File:
    File.write(JSONString)

# Check if the rule already exists:
thisFile = Path(rulesHFile)

if thisFile.is_file():
    with open(thisFile, 'r') as fp:
        content = fp.read()

        if f'struct {rule}' in content:
            print(f'Rule {rule} already exists!!')
            print(f'Quitting')

            sys.exit(0)
        else:
            print(f'OK, adding Rule {rule}')

thisFile = Path(rulesCFile)

if thisFile.is_file():
    includeTheHeader = False
else:
    includeTheHeader = True

print(f"Generating Rule {rule}")

hFile = open(rulesHFile, "a")
hFile.write(headerFile(rule, ClassName, ns))
hFile.close()

iFile = open(rulesCFile, "a")
iFile.write(implFile(rule, ClassName, ns, includeTheHeader))
iFile.close()

thisFile = Path(rulesHeaderFile)

if not thisFile.is_file():
    print(f'Generating {rulesHeaderFile}')

    hFile = open(rulesHeaderFile, 'w')
    hFile.write(rulesHeaders());
    hFile.close()
