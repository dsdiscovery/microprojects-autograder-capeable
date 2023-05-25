def kryOeQSVwYjlVkpKZohy(hoqXaivlAyWpANLYGgET):
	df_bechdel = ...
	df_bechdel
	...
	...
	...
	df = ...
	df
	if hoqXaivlAyWpANLYGgET == "_1_3":
		## == STEP 1.3 TEST CASES ==
		# - This read-only cell contains test cases for the microproject.
		# - If this cell runs without any error in the output, you PASSED all test cases!
		# - If this cell results in any errors, check you previous cells, make changes, and RE-RUN your code and then this cell.
		tada = "\N{PARTY POPPER}"

		assert( len(df) == len(df_bechdel["year"].unique()) ), \
		  "You should have one row for each year, but your `df` does not. Make sure your `index` parameter is correct."

		assert( len(df.columns) == (len(df_bechdel.columns) - 2) * 4 ), \
		  "You should have a 0,1,2,3 column for each variable. Make sure your `columns` parameter is correct. "

		assert( df["id", 0][2021] == len(df_bechdel[ (df_bechdel.year == 2021) & (df_bechdel.rating == 0) ]) ), \
		  "You have the incorrect number of movies with a 0 rating in 2021. Make sure your `aggfunc` parameter is correct."

		print(f"{tada} All tests passed! {tada}")
		return
	df = ...
	df
	if hoqXaivlAyWpANLYGgET == "_1_4":
		## == STEP 1.4 TEST CASES ==
		# - This read-only cell contains test cases for the microproject.
		# - If this cell runs without any error in the output, you PASSED all test cases!
		# - If this cell results in any errors, check you previous cells, make changes, and RE-RUN your code and then this cell.
		tada = "\N{PARTY POPPER}"

		assert( len(df) == len(df_bechdel["year"].unique()) ), \
		  "You should have one row for each year, but your `df` does not. Make sure your `index` parameter is correct."

		assert( len(df.columns) == 4 ), \
		  "You should have a single 0,1,2,3 column. Make sure your `columns` parameter is correct. "

		assert( df[3][2021] == len(df_bechdel[ (df_bechdel.year == 2021) & (df_bechdel.rating == 3) ]) ), \
		  "You have the incorrect number of movies with a 3 rating in 2021. Make sure your `aggfunc` parameter is correct."

		print(f"{tada} All tests passed! {tada}")
		return
	df = ...
	df
	if hoqXaivlAyWpANLYGgET == "_1_5":
		## == STEP 1.5 TEST CASES ==
		# - This read-only cell contains test cases for the microproject.
		# - If this cell runs without any error in the output, you PASSED all test cases!
		# - If this cell results in any errors, check you previous cells, make changes, and RE-RUN your code and then this cell.
		tada = "\N{PARTY POPPER}"

		assert( len(df) == len(df_bechdel["year"].unique()) ), \
		  "You should have one row for each year, but your `df` does not. Make sure your `index` parameter is correct."

		assert( len(df.columns) == 4 ), \
		  "You should have a single 0,1,2,3 column. Make sure your `columns` parameter is correct. "

		assert( df[3][2021] == len(df_bechdel[ (df_bechdel.year == 2021) & (df_bechdel.rating == 3) ]) ), \
		  "You have the incorrect number of movies with a 3 rating in 2021. Make sure your `aggfunc` parameter is correct."

		assert( len(df.dropna()) == len(df) ), \
		  "You have some NaN values remaining. Make sure your `fill_value` parameter is correct."

		print(f"{tada} All tests passed! {tada}")
		return
	...
	df["%0"] = ...
	df["%1"] = ...
	df["%2"] = ...
	df["%3"] = ...
	df
	if hoqXaivlAyWpANLYGgET == "_2_1":
		## == PUZZLE 2.1 TEST CASES ==
		# - This read-only cell contains test cases for the microproject.
		# - If this cell runs without any error in the output, you PASSED all test cases!
		# - If this cell results in any errors, check you previous cells, make changes, and RE-RUN your code and then this cell.
		tada = "\N{PARTY POPPER}"

		assert( "%0" in df.columns ), "Make sure you have a \"%0\" column."
		assert( "%1" in df.columns ), "Make sure you have a \"%1\" column."
		assert( "%2" in df.columns ), "Make sure you have a \"%2\" column."
		assert( "%3" in df.columns ), "Make sure you have a \"%3\" column."

		import math
		assert( math.isclose(
		        df.loc[2020]["%0"],
		        len(df_bechdel[ (df_bechdel.year == 2020) & (df_bechdel.rating == 0) ]) / len(df_bechdel[ (df_bechdel.year == 2020) ])
		      )), "Your calculation of %0 is incorrect."

		assert( math.isclose(
		        df.loc[2019]["%1"],
		        len(df_bechdel[ (df_bechdel.year == 2019) & (df_bechdel.rating == 1) ]) / len(df_bechdel[ (df_bechdel.year == 2019) ])
		      )), "Your calculation of %1 is incorrect."

		assert( math.isclose(
		        df.loc[2018]["%2"],
		        len(df_bechdel[ (df_bechdel.year == 2018) & (df_bechdel.rating == 2) ]) / len(df_bechdel[ (df_bechdel.year == 2018) ])
		      )), "Your calculation of %2 is incorrect."

		assert( math.isclose(
		        df.loc[2017]["%3"],
		        len(df_bechdel[ (df_bechdel.year == 2017) & (df_bechdel.rating == 3) ]) / len(df_bechdel[ (df_bechdel.year == 2017) ])
		      )), "Your calculation of %3 is incorrect."

		print(f"{tada} All tests passed! {tada}")
		return
	df_pct = ...
	df_pct
	if hoqXaivlAyWpANLYGgET == "_2_2":
		## == PUZZLE 2.2 TEST CASES ==
		# - This read-only cell contains test cases for the microproject.
		# - If this cell runs without any error in the output, you PASSED all test cases!
		# - If this cell results in any errors, check you previous cells, make changes, and RE-RUN your code and then this cell.
		tada = "\N{PARTY POPPER}"

		assert( "df_pct" in vars() ), "Make sure you have defined the DataFrame `df_pct`."
		assert( "%0" in df_pct.columns ), "Make sure you have a \"%0\" column."
		assert( "%1" in df_pct.columns ), "Make sure you have a \"%1\" column."
		assert( "%2" in df_pct.columns ), "Make sure you have a \"%2\" column."
		assert( "%3" in df_pct.columns ), "Make sure you have a \"%3\" column."
		assert( len(df_pct.columns) == 4 ), "Make sure you only have the percentage columns in `df_pct`."

		print(f"{tada} All tests passed! {tada}")
		return
	...

def test__1_3():
	kryOeQSVwYjlVkpKZohy("_1_3")

def test__1_4():
	kryOeQSVwYjlVkpKZohy("_1_4")

def test__1_5():
	kryOeQSVwYjlVkpKZohy("_1_5")

def test__2_1():
	kryOeQSVwYjlVkpKZohy("_2_1")

def test__2_2():
	kryOeQSVwYjlVkpKZohy("_2_2")

