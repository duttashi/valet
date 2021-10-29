### PyTest Notes

When writing pyest functions, ensure the following steps are met;
1. The test file name must begin with `test_`
2. The test body will contain the keyword `assert` `function to test`, example; 

    import user_defined_module
    
    def test_user_defined_module():
      assert user_defined_module == *expected outcome/result*

- To test the function, open terminal window, browse to directory holding python script to check/test. In terminal type, `pytest test_filename.py` and hit enter key.


