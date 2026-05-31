*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:8000

*** Test Cases ***
Inference Endpoint Returns Success

    Create Session    api    ${BASE_URL}

    ${body}=    Create Dictionary
    ...    prompt=hello

    ${response}=    POST On Session
    ...    api
    ...    /infer
    ...    json=${body}

    Status Should Be    200    ${response}

Inference Contains Expected Fields

    Create Session    api    ${BASE_URL}

    ${body}=    Create Dictionary
    ...    prompt=hello

    ${response}=    POST On Session
    ...    api
    ...    /infer
    ...    json=${body}

    ${json}=    Evaluate    $response.json()

    Dictionary Should Contain Key    ${json}    response
    Dictionary Should Contain Key    ${json}    confidence
    Dictionary Should Contain Key    ${json}    latency