Feature: Sorting a data set by a column
    Scenario: Correct parameters are passed
        Given: An input.csv file is provided
        And the csv file can be loaded into memory
        When: A heading parameter is provided
        Then: An output.csv file is generated
        And the data is sorted by the specified column in descending order

    Scenario: Parameters are missing
        Given: An input.csv file is provided
        And the csv file can be loaded into memory
        When: The program is run without a parameter
        Then: The user is prompted for a parameter
        And an output.csv file is generated
        And the specified column sorted in descending order

    Scenario: Parameter is incorrect
        Given: An input.csv file is provided
        And the csv file can be loaded into memory
        When: The program is run with a parameter
        But the parameter does not match a heading in name or case
        Then: An error is displayed
        And the program exits