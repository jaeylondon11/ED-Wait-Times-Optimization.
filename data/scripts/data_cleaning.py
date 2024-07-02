{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Cleaning\n",
    "\n",
    "In this notebook, we will clean the data from the `hospital-emergency-department-encounters-by-facility.csv` file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "# Load data\n",
    "file_path = '/mnt/data/hospital-emergency-department-encounters-by-facility.csv'\n",
    "data = pd.read_csv(file_path)\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Handling Missing Values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dropping missing values for simplicity\n",
    "data_cleaned = data.dropna()\n",
    "data_cleaned.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Removing Duplicates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Removing duplicates\n",
    "data_cleaned = data_cleaned.drop_duplicates()\n",
    "data_cleaned.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Saving the Cleaned Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save cleaned data\n",
    "processed_path = '/mnt/data/processed/'\n",
    "if not os.path.exists(processed_path):\n",
    "    os.makedirs(processed_path)\n",
    "\n",
    "data_cleaned.to_csv(os.path.join(processed_path, 'hospital_emergency_cleaned.csv'), index=False)\n",
    "print('Cleaned data saved.')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
