from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, TextClip

import constants

def create_video_of_list_of_clips(clips, output):
    print('Rendering video to location  %s' % (output))
    final_clips = []

    for clip in clips:
        path = constants.DOWNLOAD_LOCATION + clip.channel.slug + '/' + clip.slug + '.mp4'
        transitionPath = constants.DOWNLOAD_LOCATION + 'transition.mov'

        print(path)

        video = VideoFileClip(path)
        transition = VideoFileClip(transitionPath).resize( (1280,720) )
        title = TextClip(txt=clip.channel.name + ': ' + clip.title, font='Amiri-regular', color='white', fontsize=28).set_duration(8)
        title_mov = title.set_pos((0.05,0.8), relative=True)

        # Create video object with text
        final_clip = CompositeVideoClip([video, title_mov]).resize( (1280,720) )
        final_clips.append(transition)
        final_clips.append(final_clip)

        # Remove from memory
        del title
        del video
        del final_clip

    # Add clips together
    finished = concatenate_videoclips(final_clips, method='compose')

    # Render video
    finished.write_videofile(output, fps=30)