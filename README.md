{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project: Data Warehouse"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Overview"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Introduction\n",
    "A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.\n",
    "\n",
    "Data is loaded from from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Details"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The two datasets that reside in S3. Here are the S3 links for each:\n",
    "\n",
    "Song data: s3://udacity-dend/song_data\n",
    "\n",
    "Log data: s3://udacity-dend/log_data\n",
    "\n",
    "Log data json path: s3://udacity-dend/log_json_path.json"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Table Structures"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The images \"Staging.png\" and \"FandD Tables.png\" shows the structure of the staging, facts and dimension tables"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# AWS Setup Details"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\tParam\tValue\n",
    "\tDWH_CLUSTER_TYPE\tmulti-node\n",
    "\tDWH_NUM_NODES\t4\n",
    "\tDWH_NODE_TYPE\tdc2.large\n",
    "\tDWH_CLUSTER_IDENTIFIER\tdwhCluster\n",
    "\tDWH_DB\tdwh\n",
    "\tDWH_DB_USER\tdwhuser\n",
    "\tDWH_DB_PASSWORD\t***\n",
    "\tDWH_PORT\t5439\n",
    "\tDWH_IAM_ROLE_NAME\tdwhRole"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python Scripts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3 python scripts - etl.py, create_tables.py & sql_queries.py are used in this project to drop, create, load staging tables and fetch data from staging tables to the dimension and fact tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
