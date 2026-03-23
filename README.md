# Quick Startup

## UV Installation

We are going to use <code>uv</code> to install the project dependencies and libraries. 
To install run the command below on windows:

<code>powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" </code>

Then initialize uv with the following command and create a virtual environment:

<code>uv init</code>
<code>uv venv</code>

Run the following command to activate the virtual environment:
<code>.venv\Scripts\Activate.ps1</code>

## Startup:
Run the command <code> uv add -r requirements.txt </code> in your terminal to install all the dependencies.

If you don't want to keep a requirements file, then run the following command to install the dependencies:
<code>uv add numpy pandas matplotlib jupyter ipykernel torch torchvision torchaudio</code>

This would add all the dependencies in the <code>.toml</code>file and install all of them.
Furthermore it would add pytorch for NVIDIA gpu as it is the industry standard.

## Install Pytorch for Intel

To install <code>PyTorch</code> use the code given below, and since we are using <code>uv</code> the following powershell command is in uv

The device i'm currently using has an intel arc gpu so the command is for intel gpu:
<code>uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/xpu</code>

If you hav a NVIDIA gpu then follow the steps below:

>Ensure CUDA Toolkit is installed and NVIDIA drivers are up-to-date,
>Determine the appropriate CUDA version for your system from the PyTorch website's "Get Started" section (e.g.,  CUDA 12.1). Then, install PyTorch, torchvision, and torchaudio using uv, specifying the correct CUDA index URL:

<code>uv add torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121</code>
Replace cu121 with your specific CUDA version (e.g., cu118, cu124). install ipykernel.