(function() {
    let overlay = document.getElementById('reel-overlay');
    let lastVideo = null;

    const addOverlayToVideo = video => {
        const container = video.parentElement;
        if (!container) return;

        if (!overlay) {
            overlay = document.createElement('div');
            overlay.id = 'reel-overlay';
            overlay.style.position = 'absolute';
            overlay.style.top = '0';
            overlay.style.left = '0';
            overlay.style.width = '100%';
            overlay.style.height = '100%';
            overlay.style.backgroundColor = 'rgba(0,0,0,1)';
            overlay.style.zIndex = '9999';
            overlay.style.pointerEvents = 'none';
            overlay.style.display = 'flex';
            overlay.style.justifyContent = 'center';
            overlay.style.alignItems = 'center';
            
            const textElement = document.createElement('p');
            textElement.id = 'overlay-text';
            textElement.textContent = 'Liked!';
            textElement.style.color = 'white';
            textElement.style.fontSize = '48px';
            textElement.style.fontWeight = 'bold';
            textElement.style.textShadow = '2px 2px 4px rgba(0,0,0,8)';
            overlay.appendChild(textElement);

            container.style.position = 'relative';
            container.appendChild(overlay);
        } else {
            container.style.position = 'relative';
            container.appendChild(overlay);
        }

        lastVideo = video;
    };

    const handlePlay = e => {
        addOverlayToVideo(e.target);
    };

    const videos = Array.from(document.querySelectorAll('video'));
    videos.forEach(v => {
        if (!v.hasAttribute('data-overlay-listener')) {
            v.addEventListener('play', handlePlay);
            v.setAttribute('data-overlay-listener', 'true');
        }
        if (v.currentTime > 0 && !v.paused && !v.ended && v.readyState > 2) {
             addOverlayToVideo(v);
        }
    });

    const observer = new MutationObserver(() => {
        const newVideos = Array.from(document.querySelectorAll('video'));
        newVideos.forEach(v => {
            if (!v.hasAttribute('data-overlay-listener')) {
                v.addEventListener('play', handlePlay);
                v.setAttribute('data-overlay-listener', 'true');
            }
        });
    });

    observer.observe(document.body, { childList: true, subtree: true });
})();