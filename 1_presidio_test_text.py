from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

text="My phone number is 212-555-5555"

# Set up the engine, loads the NLP module (spaCy model by default) 
# and other PII recognizers
analyzer = AnalyzerEngine()

# Call analyzer to get results
results = analyzer.analyze(text=text,
                           entities=["PHONE_NUMBER"],
                           language='en')
print(results)

# Analyzer results are passed to the AnonymizerEngine for anonymization
anonymizer = AnonymizerEngine()

anonymized_text = anonymizer.anonymize(text=text,analyzer_results=results)

print(anonymized_text)