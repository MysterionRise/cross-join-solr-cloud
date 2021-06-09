import random
import uuid
import requests

states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut",
          "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho",
          "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine",
          "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota",
          "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma",
          "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
          "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia",
          "Wyoming"]

statuses = ["NOT_STARTED", "IN_PROGRESS", "COMPLETED"]


def generate_company():
    return {
        "id": uuid.uuid4().hex,
        "name": uuid.uuid4().hex
    }


def generate_companies(n=10):
    return [generate_company() for _ in range(n)]


def generate_state():
    random.choice(states)


def generate_status():
    random.choice(statuses)


def generate_project(c):
    return {
        "id": uuid.uuid4().hex,
        "name": uuid.uuid4().hex,
        "companyId": c["id"],
        "state": generate_state(),
        "status": generate_status()
    }


def generate_projects_for_company(c):
    return [generate_project(c) for _ in range(random.randint(50, 1000))]


def generate_projects(companies_list):
    return [pr for c in companies_list for pr in generate_projects_for_company(c)]


def index_json_docs(collection_name, list_of_docs, chunks_size=1000):
    chunks = [list_of_docs[i:i + 1000] for i in range(0, len(list_of_docs), 1000)]
    for chunk in chunks:
        requests.post("http://localhost:8983/solr/{}/update/json/docs?commit=true".format(collection_name),
                      json=chunk)


if __name__ == '__main__':
    companies = generate_companies(n=10000)
    projects = generate_projects(companies)
    index_json_docs("companies1", companies)
    index_json_docs("projects1", projects)
