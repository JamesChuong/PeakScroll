(function() {
    const findActiveVideo = () => {
        const videos = document.querySelectorAll('video');
        
        // Find the video that is currently playing and visible
        for (let video of videos) {
            const rect = video.getBoundingClientRect();
            const isVisible = rect.top >= 0 && rect.top < window.innerHeight;
            const isPlaying = !video.paused && !video.ended && video.currentTime > 0;
            
            if (isVisible && isPlaying) {
                return video;
            }
        }
        
        // Fallback: find the most visible video
        let mostVisibleVideo = null;
        let maxVisibleArea = 0;
        
        for (let video of videos) {
            const rect = video.getBoundingClientRect();
            const visibleHeight = Math.min(rect.bottom, window.innerHeight) - Math.max(rect.top, 0);
            const visibleArea = Math.max(0, visibleHeight) * rect.width;
            
            if (visibleArea > maxVisibleArea) {
                maxVisibleArea = visibleArea;
                mostVisibleVideo = video;
            }
        }
        
        return mostVisibleVideo;
    };

    const createRisingEmoji = (emoji, container) => {
        const emojiElement = document.createElement('div');
        emojiElement.textContent = emoji;
        emojiElement.style.position = 'absolute';
        emojiElement.style.fontSize = Math.random() * 25 + 25 + 'px';
        emojiElement.style.left = Math.random() * 90 + '%';
        emojiElement.style.bottom = '-50px';
        emojiElement.style.pointerEvents = 'none';
        emojiElement.style.userSelect = 'none';
        emojiElement.style.opacity = '0.9';
        
        container.appendChild(emojiElement);

        // Animate the rising emoji
        let position = -50;
        const speed = Math.random() * 2 + 2;

        const animate = () => {
            position += speed;
            emojiElement.style.bottom = position + 'px';
            
            // Remove emoji when it goes off screen
            if (position > container.offsetHeight + 50) {
                emojiElement.remove();
                return;
            }
            
            requestAnimationFrame(animate);
        };
        
        requestAnimationFrame(animate);
    };

    const createLaughingEmojiEffect = () => {
        // Find the currently active video
        const video = findActiveVideo();
        if (!video) return;

        const container = video.parentElement;
        if (!container) return;

        // Create overlay container if it doesn't exist
        let overlayContainer = container.querySelector('#emoji-waterfall-overlay');
        if (!overlayContainer) {
            overlayContainer = document.createElement('div');
            overlayContainer.id = 'emoji-waterfall-overlay';
            overlayContainer.style.position = 'absolute';
            overlayContainer.style.top = '0';
            overlayContainer.style.left = '0';
            overlayContainer.style.width = '100%';
            overlayContainer.style.height = '100%';
            overlayContainer.style.pointerEvents = 'none';
            overlayContainer.style.zIndex = '9999';
            overlayContainer.style.overflow = 'hidden';
            
            container.style.position = 'relative';
            container.appendChild(overlayContainer);
        }

        // Create multiple laughing emojis
        for (let i = 0; i < 10; i++) {
            setTimeout(() => {
                createRisingEmoji('😂', overlayContainer);
            }, i * 150);
        }
    };

    // Start the laughing emoji effect
    createLaughingEmojiEffect();
})();