import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams.update({'font.size': 18})

def generate_frequency_data():
    # Creating a simple signal with two frequencies
    dt = 0.001
    t = np.arange(0, 1, dt)
    f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
    f_clean = f
    f = f + 2.5*np.random.randn(len(t))

    plt.plot(t, f, c='c', lw=1.5, label='Noisy')
    plt.plot(t, f_clean, c='k', lw=2, label='Clean')
    plt.xlim(t[0], t[-1])
    plt.legend()
    plt.show()

    return dt, f_clean, f, t


def fft(dt, f_clean, f, t):
    # DO the fats forier transform to get the power spectral density:
    n = len(t)
    fhat = np.fft.fft(f, n)
    PSD = fhat * np.conj(fhat) / n
    freq = (1/(dt*n)) * np.arange(n)
    L = np.arange(1, np.floor(n/2), dtype='int')

    fig, axs = plt.subplots(2, 1)

    plt.sca(axs[0])
    plt.plot(t, f, c='c', lw=1.5, label='Noisy')
    plt.plot(t, f_clean, c='k', lw=2, label='Clean')
    plt.xlim(t[0], t[-1])
    plt.legend()

    plt.sca(axs[1])
    plt.plot(freq[L], PSD[L], c='c', lw='2', label='Noisy')
    plt.xlim(freq[L[0]], freq[L[-1]])
    plt.legend()

    plt.show()

    return PSD, fhat, freq, L


def ifft(dt, f_clean, f, t, PSD, fhat, freq, L):
    # Use the PSD to filter out fourier coefficients larger than some threshold value (100 in this case)
    indices = PSD > 100
    PSDclean = PSD * indices
    fhat = indices * fhat
    ffilt = np.fft.ifft(fhat)

    fig, axs = plt.subplots(3, 1)

    plt.sca(axs[0])
    plt.plot(t, f, c='c', lw=1.5, label='Noisy')
    plt.plot(t, f_clean, c='k', lw=2, label='Clean')
    plt.xlim(t[0], t[-1])
    plt.legend()

    plt.sca(axs[1])
    plt.plot(t, ffilt, c='k', lw='2', label='Filtered')
    plt.xlim(t[0], t[-1])
    plt.legend()

    plt.sca(axs[2])
    plt.plot(freq[L], PSD[L], c='c', lw=2, label='Noisy')
    plt.plot(freq[L], PSDclean[L], c='k', lw=1.5, label='Filtered')
    plt.xlim(freq[L[0]], freq[L[-1]])
    plt.legend()

    plt.show()


def main():
    dt, f_clean, f, t = generate_frequency_data()
    PSD, fhat, freq, L = fft(dt, f_clean, f, t)
    ifft(dt, f_clean, f, t, PSD, fhat, freq, L)

if __name__ == '__main__':
    main()


