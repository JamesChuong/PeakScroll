(function () {
    const findActiveVideo = () => {
        const videos = document.querySelectorAll('video');

        for (let video of videos) {
            const rect = video.getBoundingClientRect();
            const isVisible = rect.top >= 0 && rect.top < window.innerHeight;
            const isPlaying = !video.paused && !video.ended && video.currentTime > 0;

            if (isVisible && isPlaying) {
                return video;
            }
        }

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

    const findLikeButton = (videoElement) => {
        if (!videoElement) return null;

        let current = videoElement;
        while (current && current !== document.body) {
            // Instagram-specific selectors
            const likeButton = current.querySelector(
                'button[aria-label="Like"], ' +
                'button[aria-label="Unlike"], ' +
                'svg[aria-label="Like"], ' +
                'svg[aria-label="Unlike"], ' +
                'span[role="button"]:has(svg[aria-label*="Like"]), ' +
                'div[role="button"]:has(svg[aria-label*="Like"]), ' +
                '[data-testid="like-button"], ' +
                'button:has(svg[fill="#262626"]), ' +
                'button:has(svg[fill="#ed4956"])'
            );
            
            if (likeButton) return likeButton;
            current = current.parentElement;
        }

        // Fallback: look for heart icon SVGs
        const heartIcons = document.querySelectorAll('svg');
        for (let svg of heartIcons) {
            if (svg.getAttribute('aria-label')?.toLowerCase().includes('like')) {
                const button = svg.closest('button') || svg.closest('[role="button"]');
                if (button) return button;
            }
        }

        return null;
    };

    const likeActiveVideo = () => {
        const video = findActiveVideo();
        console.log("Active video:", video);
        
        const likeButton = findLikeButton(video);
        console.log("Like button found:", likeButton);
        
        if (likeButton) {
            // Add a small delay to ensure the page is ready
            setTimeout(() => {
                likeButton.click();
                console.log("Liked the video.");
            }, 100);
        } else {
            console.log("Like button not found. Debugging...");
            // Debug: show all potential like elements
            const allButtons = document.querySelectorAll('button, [role="button"]');
            console.log("All buttons found:", allButtons.length);
            allButtons.forEach((btn, i) => {
                if (btn.textContent.toLowerCase().includes('like') || 
                    btn.getAttribute('aria-label')?.toLowerCase().includes('like')) {
                    console.log(`Potential like button ${i}:`, btn);
                }
            });
        }
    };

    // Wait for page to be fully loaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', likeActiveVideo);
    } else {
        likeActiveVideo();
    }
})();