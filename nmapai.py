import subprocess
from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(api_key='OPEN_AI_API')

def run_nmap_command(command):
    try:
        print(f"Executing Nmap command: {command}")
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            print(f"Error in Nmap command: {stderr.decode()}")
            return None
        return stdout.decode()
    except Exception as e:
        print(f"Error executing Nmap command: {e}")
        return None

def analyze_scan(scan_output,nmap_command):
    try:
        print("Sending scan output to AI for analysis...")
        response = client.chat.completions.create(
            model="ft:gpt-3.5-turbo-0613:personal::8ghshQEx",
            messages=[{"role": "user", "content": f"This is my output from my NMAP scan {nmap_command}. Give detailed analysis to me in bullet points, and say any security feedback if necessary: {scan_output}"}],
            temperature=0.2,
            max_tokens=256,
            frequency_penalty=0.0
        )
        response_content = response.choices[0].message.content
        return response_content
    except Exception as e:
        print(f"Error during analysis: {e}")
        return None

# Get Nmap CLI command from the user
nmap_command = input("Please enter the Nmap CLI command: ")

# Run the Nmap command
print("Executing the Nmap command...")
scan_output = run_nmap_command(nmap_command)

if scan_output is None:
    print("No output from Nmap command. Exiting program.")
else:
    # Analyze the scan output
    print("Initiating the analysis of the scan output...")
    analysis = analyze_scan(scan_output,nmap_command)

    # Print the analysis directly
    if analysis:
        print("NMAP Output:")
        print(scan_output)
        print()
        print("AI Summary:")
        print(analysis)
