{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "5"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 1. Scala's real-world project repository data\n",
    "<p>With almost 30k commits and a history spanning over ten years, Scala is a mature programming language. It is a general-purpose programming language that has recently become another prominent language for data scientists.</p>\n",
    "<p>Scala is also an open source project. Open source projects have the advantage that their entire development histories -- who made changes, what was changed, code reviews, etc. -- are publicly available. </p>\n",
    "<p>We're going to read in, clean up, and visualize the real world project repository of Scala that spans data from a version control system (Git) as well as a project hosting site (GitHub). We will find out who has had the most influence on its development and who are the experts.</p>\n",
    "<p>The dataset we will use, which has been previously mined and extracted from GitHub, is comprised of three files:</p>\n",
    "<ol>\n",
    "<li><code>pulls_2011-2013.csv</code> contains the basic information about the pull requests, and spans from the end of 2011 up to (but not including) 2014.</li>\n",
    "<li><code>pulls_2014-2018.csv</code> contains identical information, and spans from 2014 up to 2018.</li>\n",
    "<li><code>pull_files.csv</code> contains the files that were modified by each pull request.</li>\n",
    "</ol>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {
    "dc": {
     "key": "5"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [],
   "source": [
    "# Importing pandas\n",
    "# ... YOUR CODE FOR TASK 1 ...\n",
    "import pandas as pd\n",
    "# Loading in the data\n",
    "pulls_one = pd.read_csv('datasets/pulls_2011-2013.csv')\n",
    "pulls_two = pd.read_csv('datasets/pulls_2014-2018.csv')\n",
    "pull_files = pd.read_csv('datasets/pull_files.csv') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "dc": {
     "key": "5"
    },
    "hide": true,
    "tags": [
     "tests"
    ]
   },
   "outputs": [
    {
     "data": {
      "application/json": "{\"success\": true, \"summary\": {\"tests\": 3, \"failures\": 0, \"errors\": 0}, \"tests\": [{\"name\": \"__main__.test_pulls_one\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_pulls_two\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_pull_files\", \"success\": true, \"message\": \"\"}]}"
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "3/3 tests passed\n"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%nose\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "def test_pulls_one():\n",
    "    correct_pulls_one = pd.read_csv('datasets/pulls_2011-2013.csv')\n",
    "    assert correct_pulls_one.equals(pulls_one), \\\n",
    "    \"Read in 'datasets/pulls_2011-2013.csv' using read_csv().\"\n",
    "\n",
    "def test_pulls_two():\n",
    "    correct_pulls_two = pd.read_csv('datasets/pulls_2014-2018.csv')\n",
    "    assert correct_pulls_two.equals(pulls_two), \\\n",
    "   \"Read in 'datasets/pulls_2014-2018.csv' using read_csv().\"\n",
    "    \n",
    "def test_pull_files():\n",
    "    correct_pull_files = pd.read_csv('datasets/pull_files.csv')\n",
    "    assert correct_pull_files.equals(pull_files), \\\n",
    "    \"Read in 'pull_files.csv' using read_csv().\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "12"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 2. Preparing and cleaning the data\n",
    "<p>First, we will need to combine the data from the two separate pull DataFrames. </p>\n",
    "<p>Next, the raw data extracted from GitHub contains dates in the ISO8601 format. However, <code>pandas</code> imports them as regular strings. To make our analysis easier, we need to convert the strings into Python's <code>DateTime</code> objects. <code>DateTime</code> objects have the important property that they can be compared and sorted.</p>\n",
    "<p>The pull request times are all in UTC (also known as Coordinated Universal Time). The commit times, however, are in the local time of the author with time zone information (number of hours difference from UTC). To make comparisons easy, we should convert all times to UTC.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {
    "dc": {
     "key": "12"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [],
   "source": [
    "# Append pulls_one to pulls_two\n",
    "pulls = pulls_one.append(pulls_two)\n",
    "\n",
    "# Convert the date for the pulls object\n",
    "pulls['date'] = pd.to_datetime(pulls['date'], utc=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "dc": {
     "key": "12"
    },
    "hide": true,
    "tags": [
     "tests"
    ]
   },
   "outputs": [
    {
     "data": {
      "application/json": "{\"success\": true, \"summary\": {\"tests\": 2, \"failures\": 0, \"errors\": 0}, \"tests\": [{\"name\": \"__main__.test_pulls_length\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_pulls_type\", \"success\": true, \"message\": \"\"}]}"
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "2/2 tests passed\n"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%nose\n",
    "\n",
    "# one or more tests of the students code. \n",
    "# The @solution should pass the tests.\n",
    "# The purpose of the tests is to try to catch common errors and to \n",
    "# give the student a hint on how to resolve these errors.\n",
    "\n",
    "def test_pulls_length():\n",
    "    assert len(pulls) == 6200, \\\n",
    "    'The DataFrame pulls does not have the correct number of rows. Did you correctly append pulls_one to pulls_two?'\n",
    "\n",
    "def test_pulls_type():\n",
    "    assert type(pulls['date'].dtype) is pd.core.dtypes.dtypes.DatetimeTZDtype, \\\n",
    "    'The date for the pull requests is not the correct type.'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "19"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 3. Merging the DataFrames\n",
    "<p>The data extracted comes in two separate files. Merging the two DataFrames will make it easier for us to analyze the data in the future tasks.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "dc": {
     "key": "19"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [],
   "source": [
    "# Merge the two DataFrames\n",
    "data = pulls.merge(pull_files, on='pid')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {
    "dc": {
     "key": "19"
    },
    "hide": true,
    "tags": [
     "tests"
    ]
   },
   "outputs": [
    {
     "data": {
      "application/json": "{\"success\": true, \"summary\": {\"tests\": 2, \"failures\": 0, \"errors\": 0}, \"tests\": [{\"name\": \"__main__.test_merge\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_merge_dataframes\", \"success\": true, \"message\": \"\"}]}"
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "2/2 tests passed\n"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%nose\n",
    "\n",
    "# one or more tests of the students code. \n",
    "# The @solution should pass the tests.\n",
    "# The purpose of the tests is to try to catch common errors and to \n",
    "# give the student a hint on how to resolve these errors.\n",
    "\n",
    "def test_merge():\n",
    "    assert len(data) == 85588, \\\n",
    "    'The merged DataFrame does not have the correct number of rows.'\n",
    "\n",
    "def test_merge_dataframes():\n",
    "    correct_data = pulls.merge(pull_files, on='pid')\n",
    "    also_correct_data = pull_files.merge(pulls, on='pid')\n",
    "    assert correct_data.equals(data) or \\\n",
    "        also_correct_data.equals(data), \\\n",
    "        \"The DataFrames are not merged correctly.\"        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "26"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 4. Is the project still actively maintained?\n",
    "<p>The activity in an open source project is not very consistent. Some projects might be active for many years after the initial release, while others can slowly taper out into oblivion. Before committing to contributing to a project, it is important to understand the state of the project. Is development going steadily, or is there a drop? Has the project been abandoned altogether?</p>\n",
    "<p>The data used in this project was collected in January of 2018. We are interested in the evolution of the number of contributions up to that date.</p>\n",
    "<p>For Scala, we will do this by plotting a chart of the project's activity. We will calculate the number of pull requests submitted each (calendar) month during the project's lifetime. We will then plot these numbers to see the trend of contributions.</p>\n",
    "<ul>\n",
    "<li><p>A helpful reminder of how to access various components of a date can be found in <a href=\"https://campus.datacamp.com/courses/data-manipulation-with-pandas/slicing-and-indexing?ex=12\">this exercise of Data Manipulation with pandas</a></p></li>\n",
    "<li><p>Additionally, recall that you can group by multiple variables by passing a list to <code>.groupby()</code>. This video from <a href=\"https://campus.datacamp.com/courses/data-manipulation-with-pandas/aggregating-dataframes?ex=9\">Data Manipulation with pandas</a> should help!</p></li>\n",
    "</ul>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {
    "dc": {
     "key": "26"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='month,year'>"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "\n",
    "# Create a column that will store the month\n",
    "data['month'] = data['date'].dt.month\n",
    "\n",
    "# Create a column that will store the year\n",
    "data['year'] = data['date'].dt.year\n",
    "\n",
    "# Group by the month and year and count the pull requests\n",
    "counts = data[['month', 'year']].value_counts()\n",
    "\n",
    "# Plot the results\n",
    "counts.plot(kind='bar', figsize = (12,4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {
    "dc": {
     "key": "26"
    },
    "hide": true,
    "tags": [
     "tests"
    ]
   },
   "outputs": [
    {
     "data": {
      "application/json": "{\"success\": true, \"summary\": {\"tests\": 1, \"failures\": 0, \"errors\": 0}, \"tests\": [{\"name\": \"__main__.test_group_and_count\", \"success\": true, \"message\": \"\"}]}"
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "1/1 tests passed\n"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%nose\n",
    "    \n",
    "def test_group_and_count():\n",
    "    assert len(counts) == 74, \\\n",
    "    \"The data was not grouped correctly. The history only spans 74 months.\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "33"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 5. Is there camaraderie in the project?\n",
    "<p>The organizational structure varies from one project to another, and it can influence your success as a contributor. A project that has a very small community might not be the best one to start working on. The small community might indicate a high barrier of entry. This can be caused by several factors, including a community that is reluctant to accept pull requests from \"outsiders,\" that the code base is hard to work with, etc. However, a large community can serve as an indicator that the project is regularly accepting pull requests from new contributors. Such a project would be a good place to start.</p>\n",
    "<p>In order to evaluate the dynamics of the community, we will plot a histogram of the number of pull requests submitted by each user. A distribution that shows that there are few people that only contribute a small number of pull requests can be used as in indicator that the project is not welcoming of new contributors. </p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {
    "dc": {
     "key": "33"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Required for matplotlib\n",
    "%matplotlib inline\n",
    "\n",
    "# Group by the submitter\n",
    "by_user = data['user'].value_counts()\n",
    "\n",
    "#Plot the histogram\n",
    "by_user.hist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "dc": {
     "key": "33"
    },
    "hide": true,
    "tags": [
     "tests"
    ]
   },
   "outputs": [
    {
     "data": {
      "application/json": "{\"success\": true, \"summary\": {\"tests\": 1, \"failures\": 0, \"errors\": 0}, \"tests\": [{\"name\": \"__main__.test_by_user\", \"success\": true, \"message\": \"\"}]}"
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "1/1 tests passed\n"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%nose\n",
    "\n",
    "# one or more tests of the students code. \n",
    "# The @solution should pass the tests.\n",
    "# The purpose of the tests is to try to catch common errors and to \n",
    "# give the student a hint on how to resolve these errors.\n",
    "\n",
    "def test_by_user():\n",
    "    assert len(by_user) == 467 or len(by_user) == 464, \\\n",
    "    'The grouping by user is not correct'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "40"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 6. What files were changed in the last ten pull requests?\n",
    "<p>Choosing the right place to make a contribution is as important as choosing the project to contribute to. Some parts of the code might be stable, some might be dead. Contributing there might not have the most impact. Therefore it is important to understand the parts of the system that have been recently changed. This allows us to pinpoint the \"hot\" areas of the code where most of the activity is happening. Focusing on those parts might not the most effective use of our times.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "dc": {
     "key": "40"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'LICENSE',\n",
       " 'doc/LICENSE.md',\n",
       " 'doc/License.rtf',\n",
       " 'project/VersionUtil.scala',\n",
       " 'src/compiler/scala/reflect/reify/phases/Calculate.scala',\n",
       " 'src/compiler/scala/tools/nsc/backend/jvm/BCodeHelpers.scala',\n",
       " 'src/compiler/scala/tools/nsc/backend/jvm/PostProcessor.scala',\n",
       " 'src/compiler/scala/tools/nsc/backend/jvm/analysis/BackendUtils.scala',\n",
       " 'src/compiler/scala/tools/nsc/profile/AsyncHelper.scala',\n",
       " 'src/compiler/scala/tools/nsc/profile/Profiler.scala',\n",
       " 'src/compiler/scala/tools/nsc/symtab/classfile/ClassfileParser.scala',\n",
       " 'src/compiler/scala/tools/nsc/typechecker/Contexts.scala',\n",
       " 'src/library/scala/Predef.scala',\n",
       " 'src/library/scala/concurrent/Lock.scala',\n",
       " 'src/library/scala/util/Properties.scala',\n",
       " 'src/reflect/scala/reflect/internal/pickling/ByteCodecs.scala',\n",
       " 'src/reflect/scala/reflect/internal/tpe/GlbLubs.scala',\n",
       " 'src/scaladoc/scala/tools/nsc/doc/html/page/Entity.scala',\n",
       " 'src/scalap/decoder.properties',\n",
       " 'test/files/neg/leibniz-liskov.check',\n",
       " 'test/files/neg/leibniz-liskov.scala',\n",
       " 'test/files/pos/leibniz-liskov.scala',\n",
       " 'test/files/pos/leibniz_liskov.scala',\n",
       " 'test/files/pos/parallel-classloader.scala',\n",
       " 'test/files/pos/t10568/Converter.java',\n",
       " 'test/files/pos/t10568/Impl.scala',\n",
       " 'test/files/pos/t10686.scala',\n",
       " 'test/files/pos/t5638/Among.java',\n",
       " 'test/files/pos/t5638/Usage.scala',\n",
       " 'test/files/pos/t9291.scala',\n",
       " 'test/files/run/t8348.check',\n",
       " 'test/files/run/t8348/TableColumn.java',\n",
       " 'test/files/run/t8348/TableColumnImpl.java',\n",
       " 'test/files/run/t8348/Test.scala'}"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Identify the last 10 pull requests\n",
    "last_10 = pulls.nlargest(10, 'date')\n",
    "\n",
    "# Join the two data sets\n",
    "joined_pr = last_10.merge(pull_files, on='pid')\n",
    "\n",
    "# Identify the unique files\n",
    "files = set(joined_pr['file'])\n",
    "\n",
    "# Print the results\n",
    "files\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {
    "dc": {
     "key": "40"
    },
    "hide": true,
    "tags": [
     "tests"
    ]
   },
   "outputs": [
    {
     "data": {
      "application/json": "{\"success\": true, \"summary\": {\"tests\": 3, \"failures\": 0, \"errors\": 0}, \"tests\": [{\"name\": \"__main__.test_last_10\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_join\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_no_files\", \"success\": true, \"message\": \"\"}]}"
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "3/3 tests passed\n"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%nose\n",
    "\n",
    "# one or more tests of the students code. \n",
    "# The @solution should pass the tests.\n",
    "# The purpose of the tests is to try to catch common errors and to \n",
    "# give the student a hint on how to resolve these errors.\n",
    "\n",
    "def test_last_10():\n",
    "    assert len(last_10) == 10, \\\n",
    "    'You need to select the last 10 pull requests.'\n",
    "\n",
    "def test_join():\n",
    "    assert len(joined_pr) == 34, \\\n",
    "    'The join was not done correctly. You lost some pull requests in the process.'\n",
    "    \n",
    "def test_no_files():\n",
    "    assert len(files) == 34, \\\n",
    "    'You did not select the right number of pull requests.'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "47"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 7. Who made the most pull requests to a given file?\n",
    "<p>When contributing to a project, we might need some guidance. We might find ourselves needing some information regarding the codebase. It is important direct any questions to the right person. Contributors to open source projects generally have other day jobs, so their time is limited. It is important to address our questions to the right people. One way to identify the right target for our inquiries is by using their contribution history.</p>\n",
    "<p>We identified <code>src/compiler/scala/reflect/reify/phases/Calculate.scala</code> as being recently changed. We are interested in the top 3 developers who changed that file. Those developers are the ones most likely to have the best understanding of the code.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "dc": {
     "key": "47"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          pid  date  file  month  year\n",
      "user                                  \n",
      "xeno-by    11    11    11     11    11\n",
      "retronym    5     5     5      5     5\n",
      "soc         4     4     4      4     4\n"
     ]
    }
   ],
   "source": [
    "# This is the file we are interested in:\n",
    "file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'\n",
    "\n",
    "# Identify the commits that changed the file\n",
    "file_pr = data[data['file'] == file]\n",
    "\n",
    "# Count the number of changes made by each developer\n",
    "author_counts = file_pr.groupby('user').count()\n",
    "\n",
    "# Print the top 3 developers\n",
    "print(author_counts.nlargest(3, 'file'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "dc": {
     "key": "47"
    },
    "hide": true,
    "tags": [
     "tests"
    ]
   },
   "outputs": [
    {
     "data": {
      "application/json": "{\"success\": true, \"summary\": {\"tests\": 2, \"failures\": 0, \"errors\": 0}, \"tests\": [{\"name\": \"__main__.test_selecting_commits\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_author_counts\", \"success\": true, \"message\": \"\"}]}"
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "2/2 tests passed\n"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%nose\n",
    "\n",
    "# one or more tests of the students code. \n",
    "# The @solution should pass the tests.\n",
    "# The purpose of the tests is to try to catch common errors and to \n",
    "# give the student a hint on how to resolve these errors.\n",
    "\n",
    "def test_selecting_commits():\n",
    "    assert len(file_pr) == 30, \\\n",
    "    'You did not filter the data on the right file.'\n",
    "    \n",
    "def test_author_counts():\n",
    "    assert len(author_counts) == 11, \\\n",
    "    'The number of authors is not correct.'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "54"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 8. Who made the last ten pull requests on a given file?\n",
    "<p>Open source projects suffer from fluctuating membership. This makes the problem of finding the right person more challenging: the person has to be knowledgeable <em>and</em> still be involved in the project. A person that contributed a lot in the past might no longer be available (or willing) to help. To get a better understanding, we need to investigate the more recent history of that particular part of the system. </p>\n",
    "<p>Like in the previous task, we will look at the history of  <code>src/compiler/scala/reflect/reify/phases/Calculate.scala</code>.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "dc": {
     "key": "54"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bjornregnell', 'retronym', 'soc', 'starblood', 'xeno-by', 'zuvizudar'}"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'\n",
    "\n",
    "# Select the pull requests that changed the target file\n",
    "file_pr = pull_files[pull_files['file'] == file]\n",
    "\n",
    "# Merge the obtained results with the pulls DataFrame\n",
    "joined_pr = file_pr.merge(pulls, on='pid')\n",
    "\n",
    "# Find the users of the last 10 most recent pull requests\n",
    "users_last_10 = set(joined_pr.nlargest(10, 'date')['user'])\n",
    "\n",
    "# Printing the results\n",
    "users_last_10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "dc": {
     "key": "54"
    },
    "hide": true,
    "tags": [
     "tests"
    ]
   },
   "outputs": [
    {
     "data": {
      "application/json": "{\"success\": true, \"summary\": {\"tests\": 3, \"failures\": 0, \"errors\": 0}, \"tests\": [{\"name\": \"__main__.test_join\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_file_pr\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_last_10\", \"success\": true, \"message\": \"\"}]}"
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "3/3 tests passed\n"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%nose\n",
    "\n",
    "# one or more tests of the students code. \n",
    "# The @solution should pass the tests.\n",
    "# The purpose of the tests is to try to catch common errors and to \n",
    "# give the student a hint on how to resolve these errors.\n",
    "\n",
    "def test_join():\n",
    "    assert len(joined_pr) == len(file_pr), \\\n",
    "    'The join was not done correctly. You lost some pull requests in the process.'\n",
    "    \n",
    "def test_file_pr():\n",
    "    assert len(joined_pr) == 30, \\\n",
    "    'The file does not have the correct number of pull requests.'\n",
    "    \n",
    "def test_last_10():\n",
    "    assert len(users_last_10) == 6, \\\n",
    "    'You did not select the right number of pull requests.'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "61"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 9. The pull requests of two special developers\n",
    "<p>Now that we have identified two potential contacts in the projects, we need to find the person who was most involved in the project in recent times. That person is most likely to answer our questions. For each calendar year, we are interested in understanding the number of pull requests the authors submitted. This will give us a high-level image of their contribution trend to the project.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "dc": {
     "key": "61"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='date'>"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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iRMnsmXLFl566SXe9ra3sXz5cs455xxaW1s57rjjuP322wG47rrr+OAHP8j06dM54ogj+MIXvvDa49x4441MmDCBY445hjlz5rzu873wwgvMmDGDcePGcd5557F9+3bmz5/PRRdd9No83/3ud7n44ovr7s1dfJLUj7W0tHDqqady6aWX8sorr3DmmWeyYMECTjzxRObPn8/GjRtpbW3l5JNPBqCtrY2HH36YwYMHM27cOC688EL23Xdf5syZw9KlSznooIN473vfy2233casWbP+7PkeeughHn/8cQ4//HCmT5/OrbfeymmnncbcuXP52te+RlNTE9deey3f+c536u7NgJKkfu6yyy6jpaWFIUOG8M1vfpPJkyezcOFCrrzySgC2bNnC008/DcBJJ53EgQd2fE42fvx4nnrqKTZs2MCUKVPYcW2+M844g/vuu6/LgGptbeXNb34zAKeffjr3338/H/rQhzjxxBNZtGgRRx99NFu3bmXChAl192VASVI/t2HDBjZv3szWrVvZsmULmcktt9zCuHHj/mS+Bx98kMGDB792f99996W9vf11H/fBBx/k3HPPBeArX/kKBxxwAB1XYPqjHfc//elPc8UVV3DUUUdx9tln90hffgYlSf3cueeey9///d9zxhlnMGfOHKZNm8ZVV11FZgJdnzi2s9bWVu69915++9vfsm3bNm688UZOOOEEJk+eTFtbG21tbZx66qlAxy6+J598ku3bt7NgwQLe/e53AzB58mTWrFnDD3/4Q04//fQe6cstKEnqSX18WPgNN9xAU1MTH/vYx9i2bRvHH388l112GQsXLmTixIls376dsWPH7vLQ8FGjRjFv3jymTp1KZjJjxgxmzpzZ5bwtLS1ccMEFrFq1iqlTp/KBD3zgtWmnnXYabW1tHHTQQT3SW+xI2EZqbm7OJUuWNLqM6qr3exsFfU9D6msrV67k6KOPbnQZRTjllFO4+OKLOemkk153nq5er4hYmpnNO8/rLj5JUl02btzIkUceydChQ3cZTnvKXXySpLoMGzaMX/3qVz3+uG5BSVKdSviopD/Y09fJgJKkOgwZMoQNGzYYUruRmWzYsIEhQ4Z0exl38UlSHUaPHs3atWtZv359o0sp3pAhQxg9enS35zegJKkOTU1NjB07ttFlDEju4pMkFcmAkiQVyYCSJBXJgJIkFcmA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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "\n",
    "# The developers we are interested in\n",
    "authors = ['xeno-by', 'soc']\n",
    "\n",
    "# Get all the developers' pull requests\n",
    "by_author = pulls[pulls['user'].isin(authors)]\n",
    "\n",
    "# Count the number of pull requests submitted each year\n",
    "counts = by_author.groupby(['user', by_author['date'].dt.year]).agg({'pid': 'count'}).reset_index()\n",
    "\n",
    "# Convert the table to a wide format\n",
    "counts_wide = counts.pivot_table(index='date', columns='user', values='pid', fill_value=0)\n",
    "\n",
    "# Plot the results\n",
    "counts_wide.plot(kind='bar')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {
    "dc": {
     "key": "61"
    },
    "hide": true,
    "tags": [
     "tests"
    ]
   },
   "outputs": [
    {
     "data": {
      "application/json": "{\"success\": true, \"summary\": {\"tests\": 2, \"failures\": 0, \"errors\": 0}, \"tests\": [{\"name\": \"__main__.test_author_pr\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_counts\", \"success\": true, \"message\": \"\"}]}"
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "2/2 tests passed\n"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%nose\n",
    "\n",
    "# one or more tests of the students code. \n",
    "# The @solution should pass the tests.\n",
    "# The purpose of the tests is to try to catch common errors and to \n",
    "# give the student a hint on how to resolve these errors.\n",
    "\n",
    "def test_author_pr():\n",
    "    assert len(by_author) == 715, \\\n",
    "    \"The wrong number of pull requests have been selected.\"\n",
    "    \n",
    "def test_counts():\n",
    "    assert len(counts) == 11, \\\n",
    "    'The data should span 6 years.'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "dc": {
     "key": "68"
    },
    "deletable": false,
    "editable": false,
    "run_control": {
     "frozen": true
    },
    "tags": [
     "context"
    ]
   },
   "source": [
    "## 10. Visualizing the contributions of each developer\n",
    "<p>As mentioned before, it is important to make a distinction between the global expertise and contribution levels and the contribution levels at a more granular level (file, submodule, etc.) In our case, we want to see which of our two developers of interest have the most experience with the code in a given file. We will measure experience by the number of pull requests submitted that affect that file and how recent those pull requests were submitted.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {
    "dc": {
     "key": "68"
    },
    "tags": [
     "sample_code"
    ]
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='date'>"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "authors = ['xeno-by', 'soc']\n",
    "file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'\n",
    "\n",
    "# Select the pull requests submitted by the authors, from the `data` DataFrame\n",
    "by_author = data[data['user'].isin(authors)]\n",
    "\n",
    "# Select the pull requests that affect the file\n",
    "by_file = by_author[by_author['file'] == file]\n",
    "\n",
    "# Group and count the number of PRs done by each user each year\n",
    "grouped = by_file.groupby(['user', by_file['date'].dt.year]).count()['pid'].reset_index()\n",
    "\n",
    "# Transform the data into a wide format\n",
    "by_file_wide = grouped.pivot_table(index='date', columns='user', values='pid', fill_value=0)\n",
    "\n",
    "# Plot the results\n",
    "by_file_wide.plot(kind='bar')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {
    "dc": {
     "key": "68"
    },
    "hide": true,
    "tags": [
     "tests"
    ]
   },
   "outputs": [
    {
     "data": {
      "application/json": "{\"success\": true, \"summary\": {\"tests\": 3, \"failures\": 0, \"errors\": 0}, \"tests\": [{\"name\": \"__main__.test_by_author\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_by_file\", \"success\": true, \"message\": \"\"}, {\"name\": \"__main__.test_by_file_wide\", \"success\": true, \"message\": \"\"}]}"
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "3/3 tests passed\n"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%nose\n",
    "\n",
    "# one or more tests of the students code. \n",
    "# The @solution should pass the tests.\n",
    "# The purpose of the tests is to try to catch common errors and to \n",
    "# give the student a hint on how to resolve these errors.\n",
    "\n",
    "def test_by_author():\n",
    "    assert len(by_author) == 16999, \\\n",
    "    'Selecting by author did not produce the expected results.'\n",
    "    \n",
    "def test_by_file():\n",
    "    assert len(by_file) == 15, \\\n",
    "    'Selecting by file did not produce the expected results.'\n",
    "    \n",
    "# def test_grouped():\n",
    "#     assert len(grouped) == 4, \\\n",
    "#     'There should be only 3 years that matches our data.'\n",
    "    \n",
    "def test_by_file_wide():\n",
    "    assert len(by_file_wide) == 3, \\\n",
    "    'There should be only 3 years that matches our data.'"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
